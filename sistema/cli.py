"""Interface de estudo, independente de IA, editor ou serviço externo."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys

from sistema.trilha import (
    ErroTrilha, carregar_curriculo, carregar_progresso, conferir_integridade,
    concluir, executar_aula, quantidade_validas,
)

RAIZ = Path(__file__).resolve().parents[1]


def ambiente():
    print(f"Python: {sys.version.split()[0]}")
    print(f"Executável: {sys.executable}")
    try:
        import sqlite3
        import unittest
        conexao = sqlite3.connect(":memory:")
        conexao.execute("SELECT 1").fetchone()
        conexao.close()
        print(f"Biblioteca padrão: unittest disponível; SQLite {sqlite3.sqlite_version} disponível.")
    except ImportError as erro:
        raise ErroTrilha(f"Instalação incompleta do Python: {erro}. Consulte README.md.") from erro
    if shutil.which("git"):
        resultado = subprocess.run(["git", "--version"], capture_output=True, text=True, timeout=10)
        print(resultado.stdout.strip() or "Git encontrado; confira git --version manualmente.")
    else:
        print("Git não encontrado. Os estudos funcionam; para clonar e versionar, instale conforme README.md.")
    print("Nenhum pacote pip é necessário. Ambiente pronto para os estudos.")
    return 0


def parser_cli():
    parser = argparse.ArgumentParser(description="Trilha local de Python: leia, implemente, teste e acompanhe seu progresso.")
    comandos = parser.add_subparsers(dest="comando")
    comandos.add_parser("ambiente", help="confere Python, SQLite e Git")
    comandos.add_parser("listar", help="mostra todas as aulas e o progresso")
    comandos.add_parser("continuar", help="mostra o material da aula atual")
    comandos.add_parser("status", help="mostra a posição e o total concluído")
    aula = comandos.add_parser("aula", help="mostra o material de uma aula sem mudar a posição")
    aula.add_argument("numero", nargs="?", help="número da aula, por exemplo 05")
    testar = comandos.add_parser("testar", help="executa os testes públicos de uma aula")
    selecao = testar.add_mutually_exclusive_group()
    selecao.add_argument("numero", nargs="?", help="número da aula; padrão é a aula atual")
    selecao.add_argument("--todas", action="store_true", help="inclui práticas futuras, que inicialmente falham")
    selecao.add_argument("--concluidas", action="store_true", help="testa todas as aulas registradas no progresso")
    conclusao = comandos.add_parser("concluir", help="testa e registra a aula atual, respeitando pré-requisitos")
    conclusao.add_argument("--revisei", action="store_true", help="confirma que você conferiu o checklist do enunciado")
    comandos.add_parser("verificar", help="valida os arquivos da trilha e testa o sistema, sem exigir práticas resolvidas")
    return parser


def encontrar(aulas, numero):
    try:
        identificador = f"{int(numero):02d}"
    except (ValueError, TypeError):
        raise ErroTrilha("Use um número de aula, como 01 ou 12.") from None
    for aula in aulas:
        if aula["id"] == identificador:
            return aula
    raise ErroTrilha(f"Aula {numero} não existe. Use listar para ver os números disponíveis.")


def mostrar(aula):
    print(f"\nAula {aula['id']} — {aula['titulo']}")
    print(f"Estudo:  {aula['conceito']}")
    print(f"Prática: {aula['pratica']}")
    print(f"Teste:   {aula['teste']}")
    interpretador = "py -3" if sys.platform == "win32" else "python3"
    print(f"Após implementar: {interpretador} estudar.py testar {aula['id']}")
    print("Abra os caminhos acima no editor. Use estudos/README.md para links clicáveis.")


def main(argv=None, raiz=None):
    raiz = RAIZ if raiz is None else Path(raiz)
    argumentos = parser_cli().parse_args(argv)
    comando = argumentos.comando or "continuar"
    try:
        if comando == "ambiente":
            return ambiente()
        aulas = carregar_curriculo(raiz)
        if comando == "verificar":
            from sistema.validacao import verificar_estrutura
            conferir_integridade(raiz)
            erros = verificar_estrutura(raiz, aulas)
            if erros:
                raise ErroTrilha("\n".join(erros))
            print(f"Estrutura válida: {len(aulas)} aulas e {sum(a['casos'] for a in aulas)} casos públicos.", flush=True)
            resultado = subprocess.run([sys.executable, "-B", "-X", "utf8", "-m", "unittest", "discover", "-s", "testes_sistema", "-v"], cwd=raiz, timeout=60)
            if resultado.returncode == 0:
                print("Sistema pronto. As práticas do aluno permanecem para você resolver.")
            return 0 if resultado.returncode == 0 else 1
        if comando == "concluir":
            return concluir(raiz, aulas, argumentos.revisei)
        progresso = carregar_progresso(raiz, aulas)
        validas = quantidade_validas(raiz, aulas, progresso)
        atual = aulas[validas] if validas < len(aulas) else None
        if comando == "listar":
            for indice, aula in enumerate(aulas):
                estado = "CONCLUÍDA" if indice < validas else ("ATUAL" if indice == validas else "PENDENTE")
                print(f"{aula['id']} [{estado:9}] {aula['titulo']} ({aula['tipo']})")
        elif comando in {"continuar", "status", "aula"}:
            print(f"Progresso: {validas}/{len(aulas)} aulas concluídas com arquivos ainda correspondentes à avaliação.")
            if len(progresso["concluidas"]) > validas:
                print("Uma prática concluída foi alterada: retome a primeira aula modificada para revalidar os pré-requisitos. Veja docs/PROGRESSO.md.")
            escolhida = encontrar(aulas, argumentos.numero) if comando == "aula" and argumentos.numero else atual
            if escolhida:
                mostrar(escolhida)
            else:
                print("Trilha concluída. Materiais e testes continuam disponíveis para revisão.")
        elif comando == "testar":
            conferir_integridade(raiz)
            if argumentos.todas:
                escolhidas = aulas
            elif argumentos.concluidas:
                escolhidas = [a for a in aulas if a["id"] in progresso["concluidas"]]
            elif argumentos.numero:
                escolhidas = [encontrar(aulas, argumentos.numero)]
            else:
                escolhidas = [atual] if atual else []
            if not escolhidas:
                print("Nenhuma aula selecionada. Use testar NÚMERO ou testar --todas.")
                return 0
            resultados = [executar_aula(raiz, aula) for aula in escolhidas]
            print(f"\nResultado: {sum(resultados)}/{len(resultados)} aulas passaram. Testar não altera o progresso.")
            return 0 if all(resultados) else 1
        return 0
    except (ErroTrilha, OSError, subprocess.TimeoutExpired) as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nExecução interrompida. Consulte status antes de retomar.", file=sys.stderr)
        return 130

"""Currículo, execução local e progresso. Não depende de pacotes externos."""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


class ErroTrilha(Exception):
    """Falha que pode ser apresentada ao aluno sem traceback interno."""


def ler_json(caminho):
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, ValueError) as erro:
        raise ErroTrilha(f"Não foi possível ler {caminho}: {erro}. O arquivo foi preservado.") from erro


def carregar_curriculo(raiz):
    dados = ler_json(raiz / "curriculum/python.json")
    if not isinstance(dados, dict) or dados.get("versao") != 1 or not isinstance(dados.get("aulas"), list) or not dados["aulas"]:
        raise ErroTrilha("Currículo inválido. Restaure curriculum/python.json da cópia original.")
    ids = []
    for numero, aula in enumerate(dados["aulas"], 1):
        if not isinstance(aula, dict) or aula.get("id") != f"{numero:02d}":
            raise ErroTrilha("A sequência do currículo está inválida.")
        for campo in ["titulo", "modulo", "tipo", "conceito", "pratica", "teste", "modulo_teste"]:
            if not isinstance(aula.get(campo), str):
                raise ErroTrilha(f"Campo {campo} inválido no currículo.")
        if not isinstance(aula.get("arquivos"), list) or not aula["arquivos"] or not all(isinstance(p, str) for p in aula["arquivos"]):
            raise ErroTrilha("Lista de arquivos inválida no currículo.")
        if type(aula.get("casos")) is not int or aula["casos"] < 1:
            raise ErroTrilha("Quantidade de casos inválida no currículo.")
        if aula.get("pre_requisitos") != ([ids[-1]] if ids else []):
            raise ErroTrilha("Pré-requisitos do currículo inválidos.")
        for relativo in [aula["conceito"], aula["pratica"], aula["teste"], *aula["arquivos"]]:
            caminho = raiz / relativo
            if not caminho.resolve().is_relative_to(raiz.resolve()) or not caminho.is_file():
                raise ErroTrilha(f"Arquivo ausente ou fora do projeto: {relativo}")
        ids.append(aula["id"])
    return dados["aulas"]


def assinatura(raiz, aula):
    """Inclui os arquivos declarados e novos módulos Python da pasta da atividade."""
    arquivos = set(aula["arquivos"])
    pasta = (raiz / aula["arquivos"][0]).parent
    arquivos.update(str(p.relative_to(raiz)).replace(os.sep, "/") for p in pasta.rglob("*.py"))
    resumo = hashlib.sha256()
    for relativo in sorted(arquivos):
        caminho = raiz / relativo
        resumo.update(relativo.encode("utf-8") + b"\0")
        resumo.update(caminho.read_bytes())
        resumo.update(b"\0")
    return resumo.hexdigest()


def carregar_progresso(raiz, aulas):
    caminho = raiz / ".learning/progress.json"
    if not caminho.exists():
        return {"versao": 1, "concluidas": {}}
    dados = ler_json(caminho)
    valido = isinstance(dados, dict) and dados.get("versao") == 1 and isinstance(dados.get("concluidas"), dict)
    if valido:
        registros = dados["concluidas"]
        ids = [aula["id"] for aula in aulas]
        valido = set(registros) == set(ids[:len(registros)])
        for registro in registros.values():
            if not isinstance(registro, dict) or not isinstance(registro.get("concluida_em"), str) or not isinstance(registro.get("assinatura"), str):
                valido = False
                break
            if len(registro["assinatura"]) != 64 or any(c not in "0123456789abcdef" for c in registro["assinatura"]):
                valido = False
                break
    if not valido:
        raise ErroTrilha("Progresso inválido; nenhum dado foi sobrescrito. Consulte docs/PROGRESSO.md para recuperar o backup.")
    return dados


def quantidade_validas(raiz, aulas, progresso):
    quantidade = 0
    for aula in aulas:
        registro = progresso["concluidas"].get(aula["id"])
        if not registro or registro["assinatura"] != assinatura(raiz, aula):
            break
        quantidade += 1
    return quantidade


def gravar_atomico(caminho, conteudo):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=caminho.parent, delete=False) as arquivo:
            temporario = Path(arquivo.name)
            arquivo.write(conteudo)
            arquivo.flush()
            os.fsync(arquivo.fileno())
        os.replace(temporario, caminho)
    finally:
        if temporario is not None and temporario.exists():
            temporario.unlink()


@contextmanager
def trava_progresso(raiz):
    pasta = raiz / ".learning"
    pasta.mkdir(exist_ok=True)
    caminho = pasta / "conclusao.lock"
    try:
        descritor = os.open(caminho, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as erro:
        raise ErroTrilha("Há uma conclusão em andamento. Se ela foi interrompida, veja docs/PROGRESSO.md antes de remover .learning/conclusao.lock.") from erro
    try:
        with os.fdopen(descritor, "w", encoding="utf-8") as arquivo:
            arquivo.write(str(os.getpid()))
        yield
    finally:
        caminho.unlink(missing_ok=True)


def conferir_integridade(raiz):
    manifesto = ler_json(raiz / "curriculum/integridade.json")
    if not isinstance(manifesto, dict) or manifesto.get("versao") != 1 or not isinstance(manifesto.get("arquivos"), dict) or not manifesto["arquivos"]:
        raise ErroTrilha("Manifesto de integridade inválido.")
    alterados = []
    for relativo, esperado in manifesto["arquivos"].items():
        caminho = raiz / relativo
        if not caminho.resolve().is_relative_to(raiz.resolve()) or not caminho.is_file() or hashlib.sha256(caminho.read_bytes()).hexdigest() != esperado:
            alterados.append(relativo)
    if alterados:
        raise ErroTrilha("Arquivos de avaliação alterados ou ausentes: " + ", ".join(alterados) + ". Preserve suas práticas e restaure esses arquivos da cópia original. Veja docs/PROGRESSO.md.")


def executar_aula(raiz, aula, tempo=45):
    print(f"\nAula {aula['id']} — {aula['titulo']} ({aula['casos']} casos públicos)", flush=True)
    ambiente = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="python-trilha-") as pasta:
        comprovante = Path(pasta) / "resultado.json"
        try:
            processo = subprocess.run(
                [sys.executable, "-B", "-X", "utf8", "-m", "sistema.executar", aula["modulo_teste"], str(comprovante)],
                cwd=raiz, env=ambiente, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=tempo,
            )
        except subprocess.TimeoutExpired:
            print(f"O teste ultrapassou {tempo:g} segundos. Confira laços sem fim ou esperas indevidas. Progresso não registrado.")
            return False
        if processo.stdout:
            print(processo.stdout, end="")
        if processo.stderr:
            print(processo.stderr, end="")
        if not comprovante.exists():
            print("A suíte não terminou normalmente. Um exit, erro de importação ou encerramento antecipado não aprova a aula.")
            return False
        resultado = ler_json(comprovante)
        passou = (
            processo.returncode == 0 and resultado.get("sucesso") is True
            and resultado.get("executados") == aula["casos"]
            and all(resultado.get(campo) == 0 for campo in ["falhas", "erros", "pulados", "falhas_esperadas", "sucessos_inesperados"])
        )
        if not passou:
            print(f"Aula pendente. Consulte {aula['pratica']} e docs/COMO_LER_TESTES.md. Nenhuma conclusão foi registrada.")
        return passou


def concluir(raiz, aulas, revisei):
    if not revisei:
        print("Confira a autoavaliação no enunciado da aula atual. Depois use: concluir --revisei")
        return 2
    conferir_integridade(raiz)
    with trava_progresso(raiz):
        progresso = carregar_progresso(raiz, aulas)
        indice = quantidade_validas(raiz, aulas, progresso)
        if indice == len(aulas):
            print("Trilha concluída. Você pode revisitar os materiais e testar qualquer aula.")
            return 0
        aula = aulas[indice]
        antes = assinatura(raiz, aula)
        if not executar_aula(raiz, aula):
            return 1
        conferir_integridade(raiz)
        if assinatura(raiz, aula) != antes:
            raise ErroTrilha("A prática mudou durante os testes. Execute concluir novamente após salvar suas edições.")
        # Também impede registrar sobre pré-requisitos editados durante a execução.
        if quantidade_validas(raiz, aulas, progresso) != indice:
            raise ErroTrilha("Um pré-requisito mudou durante os testes. Retome com continuar.")
        agora = datetime.now(timezone.utc).isoformat(timespec="seconds")
        registros = {anterior["id"]: progresso["concluidas"][anterior["id"]] for anterior in aulas[:indice]}
        registros[aula["id"]] = {"concluida_em": agora, "assinatura": antes}
        caminho = raiz / ".learning/progress.json"
        if caminho.exists():
            gravar_atomico(caminho.with_suffix(".json.bak"), caminho.read_text(encoding="utf-8"))
        gravar_atomico(caminho, json.dumps({"versao": 1, "concluidas": registros}, ensure_ascii=False, indent=2) + "\n")
        proxima = aulas[indice + 1]["conceito"] if indice + 1 < len(aulas) else "Trilha concluída"
        gravar_atomico(raiz / ".learning/session.md", f"# Última sessão\n\nAula {aula['id']} — {aula['titulo']} concluída em {agora} (UTC).\n\nTestes públicos completos e autoavaliação confirmada pelo aluno.\n\nPróximo material: {proxima}\n")
        with (raiz / ".learning/history.md").open("a", encoding="utf-8") as historico:
            historico.write(f"- {agora}: conclusão da aula {aula['id']} — {aula['titulo']}.\n")
        print(f"\nAula {aula['id']} concluída e progresso salvo. Próximo: {proxima}")
        if indice >= 1:
            print("Revise git status e git diff; prepare os arquivos da atividade e faça um commit pequeno na sua cópia.")
        if aula["tipo"] in {"checkpoint", "projeto_final"}:
            print("Se usa GitHub, confira seu remoto e sincronize sua cópia após revisar o commit.")
        return 0

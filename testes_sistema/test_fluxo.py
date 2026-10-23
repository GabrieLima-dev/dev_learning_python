"""Regressões do sistema, sempre em cópias temporárias; não resolvem a prática do aluno."""
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from sistema.trilha import (
    ErroTrilha, carregar_curriculo, carregar_progresso, conferir_integridade,
    executar_aula, gravar_atomico, quantidade_validas, trava_progresso,
)
from sistema.validacao import verificar_estrutura

ORIGINAL = Path(__file__).resolve().parents[1]


class TestSistema(unittest.TestCase):
    def setUp(self):
        self.temporario = tempfile.TemporaryDirectory(prefix="teste-trilha-")
        self.addCleanup(self.temporario.cleanup)
        self.raiz = Path(self.temporario.name) / "projeto com espaços e acentos á"
        shutil.copytree(ORIGINAL, self.raiz, ignore=shutil.ignore_patterns(
            ".git", ".learning", ".montagem", "__pycache__", ".venv", ".DS_Store",
        ))
        self.aulas = carregar_curriculo(self.raiz)
        # Os testes do sistema não dependem do estágio real das práticas do aluno.
        # Estes esqueletos são gravados SOMENTE na cópia temporária de cada teste.
        (self.raiz / self.aulas[0]["arquivos"][0]).write_text(
            'def mensagem_inicial():\n    raise NotImplementedError("fixture pendente")\n', encoding="utf-8",
        )
        (self.raiz / self.aulas[1]["arquivos"][0]).write_text(
            'COMANDO_ESTADO = ""\nCOMANDO_DIFERENCAS = ""\n'
            'COMANDO_PREPARADO = ""\nPASTA_LOCAL = ""\n', encoding="utf-8",
        )

    def cli(self, *args, sucesso=None):
        ambiente = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
        resultado = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(self.raiz / "estudar.py"), *args],
            cwd=self.raiz.parent, env=ambiente, capture_output=True,
            text=True, encoding="utf-8", timeout=15,
        )
        if sucesso is not None:
            self.assertEqual(resultado.returncode, sucesso, resultado.stdout + resultado.stderr)
        return resultado

    def resolver_primeira(self):
        (self.raiz / self.aulas[0]["arquivos"][0]).write_text(
            'def mensagem_inicial():\n    return "Minha jornada em Python começou!"\n', encoding="utf-8",
        )

    def resolver_segunda(self):
        (self.raiz / self.aulas[1]["arquivos"][0]).write_text(
            'COMANDO_ESTADO = "git status"\nCOMANDO_DIFERENCAS = "git diff"\n'
            'COMANDO_PREPARADO = "git diff --staged"\nPASTA_LOCAL = ".learning/"\n', encoding="utf-8",
        )

    def progresso(self):
        return carregar_progresso(self.raiz, self.aulas)

    def test_clone_limpo_tem_estrutura_integra_sem_progresso(self):
        conferir_integridade(self.raiz)
        self.assertEqual(verificar_estrutura(self.raiz, self.aulas), [])
        self.assertEqual(self.progresso()["concluidas"], {})
        self.assertEqual(len(self.aulas), 32)

    def test_continuar_sem_estado_nao_grava_e_funciona_fora_da_raiz(self):
        resultado = self.cli("continuar", sucesso=0)
        self.assertIn("Aula 01", resultado.stdout)
        self.assertFalse((self.raiz / ".learning").exists())

    def test_consultar_aula_futura_nao_avanca(self):
        self.assertIn("Aula 32", self.cli("aula", "32", sucesso=0).stdout)
        self.assertIn("Aula 01", self.cli("status", sucesso=0).stdout)
        self.assertEqual(self.progresso()["concluidas"], {})

    def test_aula_inexistente_gera_mensagem_clara(self):
        resultado = self.cli("aula", "999", sucesso=2)
        self.assertIn("não existe", resultado.stderr)
        self.assertNotIn("Traceback", resultado.stderr)

    def test_pratica_incompleta_nao_conclui_nem_sobrescreve(self):
        arquivo = self.raiz / self.aulas[0]["arquivos"][0]
        antes = arquivo.read_bytes()
        self.cli("concluir", "--revisei", sucesso=1)
        self.assertFalse((self.raiz / ".learning/progress.json").exists())
        self.assertEqual(arquivo.read_bytes(), antes)
        self.assertFalse((self.raiz / ".learning/conclusao.lock").exists())

    def test_conclusao_exige_autoavaliacao(self):
        self.resolver_primeira()
        self.cli("concluir", sucesso=2)
        self.assertEqual(self.progresso()["concluidas"], {})

    def test_testar_verde_nao_registra_progresso(self):
        self.resolver_primeira()
        self.cli("testar", "01", sucesso=0)
        self.assertEqual(self.progresso()["concluidas"], {})

    def test_concluir_salva_retomada_backup_e_historico(self):
        self.resolver_primeira()
        self.cli("concluir", "--revisei", sucesso=0)
        self.assertIn("Aula 02", self.cli("continuar", sucesso=0).stdout)
        self.assertEqual(set(self.progresso()["concluidas"]), {"01"})
        self.resolver_segunda()
        self.cli("concluir", "--revisei", sucesso=0)
        self.assertEqual(set(self.progresso()["concluidas"]), {"01", "02"})
        backup = json.loads((self.raiz / ".learning/progress.json.bak").read_text())
        self.assertEqual(set(backup["concluidas"]), {"01"})
        self.assertIn("aula 02", (self.raiz / ".learning/history.md").read_text())
        self.assertIn("Aula 02", (self.raiz / ".learning/session.md").read_text())

    def test_falha_na_segunda_preserva_primeira_conclusao(self):
        self.resolver_primeira()
        self.cli("concluir", "--revisei", sucesso=0)
        caminho = self.raiz / ".learning/progress.json"
        antes = caminho.read_bytes()
        self.cli("concluir", "--revisei", sucesso=1)
        self.assertEqual(caminho.read_bytes(), antes)

    def test_alterar_concluida_reabre_cadeia_e_descarta_conclusoes_posteriores_ao_revalidar(self):
        self.resolver_primeira()
        self.resolver_segunda()
        self.cli("concluir", "--revisei", sucesso=0)
        self.cli("concluir", "--revisei", sucesso=0)
        arquivo = self.raiz / self.aulas[0]["arquivos"][0]
        arquivo.write_text(arquivo.read_text() + "\n# comentário novo\n", encoding="utf-8")
        self.assertEqual(quantidade_validas(self.raiz, self.aulas, self.progresso()), 0)
        self.assertIn("alterada", self.cli("status", sucesso=0).stdout)
        self.cli("concluir", "--revisei", sucesso=0)
        self.assertEqual(set(self.progresso()["concluidas"]), {"01"})
        self.assertIn("Aula 02", self.cli("continuar", sucesso=0).stdout)

    def test_testes_alterados_bloqueiam_conclusao(self):
        self.resolver_primeira()
        arquivo = self.raiz / self.aulas[0]["teste"]
        arquivo.write_text(arquivo.read_text() + "\n# edição acidental\n", encoding="utf-8")
        resultado = self.cli("concluir", "--revisei", sucesso=2)
        self.assertIn("avaliação alterados", resultado.stderr)
        self.assertEqual(self.progresso()["concluidas"], {})

    def test_estado_corrompido_preservado(self):
        pasta = self.raiz / ".learning"
        pasta.mkdir()
        caminho = pasta / "progress.json"
        caminho.write_text("{quebrado", encoding="utf-8")
        self.cli("status", sucesso=2)
        self.assertEqual(caminho.read_text(), "{quebrado")

    def test_estado_com_salto_de_prerequisito_rejeitado(self):
        pasta = self.raiz / ".learning"
        pasta.mkdir()
        caminho = pasta / "progress.json"
        caminho.write_text(json.dumps({"versao": 1, "concluidas": {"02": {"assinatura": "a" * 64, "concluida_em": "data"}}}), encoding="utf-8")
        with self.assertRaises(ErroTrilha):
            self.progresso()

    def test_saida_zero_prematura_nao_aprova(self):
        (self.raiz / self.aulas[0]["arquivos"][0]).write_text("import os\nos._exit(0)\n", encoding="utf-8")
        resultado = self.cli("testar", "01", sucesso=1)
        self.assertIn("não terminou normalmente", resultado.stdout)

    def test_timeout_encerra_teste_sem_concluir(self):
        (self.raiz / self.aulas[0]["arquivos"][0]).write_text("import time\ntime.sleep(5)\n", encoding="utf-8")
        with redirect_stdout(io.StringIO()) as saida:
            passou = executar_aula(self.raiz, self.aulas[0], tempo=0.1)
        self.assertFalse(passou)
        self.assertIn("ultrapassou", saida.getvalue())
        self.assertEqual(self.progresso()["concluidas"], {})

    def test_testes_pulados_nao_sao_sucesso(self):
        arquivo = self.raiz / self.aulas[0]["teste"]
        arquivo.write_text('import unittest\n@unittest.skip("simulação")\nclass Caso(unittest.TestCase):\n    def test_a(self):\n        pass\n    def test_b(self):\n        pass\n', encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            self.assertFalse(executar_aula(self.raiz, self.aulas[0]))

    def test_prerequisito_bloqueia_pular_para_exercicio_resolvido(self):
        self.resolver_segunda()
        self.cli("testar", "02", sucesso=0)
        self.cli("concluir", "--revisei", sucesso=1)
        self.assertEqual(self.progresso()["concluidas"], {})

    def test_trava_impede_duas_conclusoes_e_e_liberada(self):
        with trava_progresso(self.raiz):
            with self.assertRaises(ErroTrilha):
                with trava_progresso(self.raiz):
                    pass
        self.assertFalse((self.raiz / ".learning/conclusao.lock").exists())

    def test_gravacao_atomica_substitui_conteudo_e_nao_deixa_temporario(self):
        caminho = self.raiz / "rascunho/estado.json"
        gravar_atomico(caminho, "antes")
        gravar_atomico(caminho, "depois")
        self.assertEqual(caminho.read_text(), "depois")
        self.assertEqual(list(caminho.parent.iterdir()), [caminho])

    def test_validador_identifica_link_quebrado(self):
        documento = self.raiz / self.aulas[0]["conceito"]
        documento.write_text(documento.read_text() + "\n[Link](nao_existe.md)\n", encoding="utf-8")
        self.assertTrue(any("nao_existe.md" in erro for erro in verificar_estrutura(self.raiz, self.aulas)))

    def test_curriculo_sem_arquivo_e_rejeitado(self):
        (self.raiz / self.aulas[0]["conceito"]).unlink()
        with self.assertRaises(ErroTrilha):
            carregar_curriculo(self.raiz)

    def test_selecao_de_teste_incompativel_gera_erro_de_uso(self):
        self.cli("testar", "01", "--todas", sucesso=2)


if __name__ == "__main__":
    unittest.main()

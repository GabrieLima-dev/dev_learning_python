"""Casos públicos da aula 32. Cada A32-NN está descrito em PRATICA.md."""

import unittest
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout, redirect_stderr
from testes.apoio import Contrato

ROOT = Path(__file__).resolve().parents[1]

from praticas.aula32_projeto_final import pratica as p


class TestAula32(Contrato):

    def test_A32_01(self):
        r"""A32-01: Banco vazio lista []; adicionar ' Estudar ' e 'Estudar' gera IDs 1 e 2, pendentes, com títulos normalizados."""
        with tempfile.TemporaryDirectory() as pasta:
            repo = p.RepositorioTarefas(Path(pasta) / "tarefas.sqlite3")
            self.assertValor(repo.listar(), [])
            self.assertValor(repo.adicionar(" Estudar "), 1)
            self.assertValor(repo.adicionar("Estudar"), 2)
            self.assertValor(repo.listar(), [{"id": 1, "titulo": "Estudar", "concluida": False}, {"id": 2, "titulo": "Estudar", "concluida": False}])

    def test_A32_02(self):
        r"""A32-02: Título de 80 caracteres aceito; vazio, espaços e 81 caracteres rejeitados sem inserir."""
        with tempfile.TemporaryDirectory() as pasta:
            repo = p.RepositorioTarefas(Path(pasta) / "tarefas.sqlite3")
            self.assertValor(repo.adicionar("a" * 80), 1)
            for titulo in ["", "   ", "a" * 81]:
                with self.assertRaises(ValueError) as erro:
                    repo.adicionar(titulo)
                self.assertEqual(str(erro.exception), "título inválido")
            self.assertEqual(len(repo.listar()), 1)

    def test_A32_03(self):
        r"""A32-03: Concluir id 1 duas vezes retorna True; id 99 retorna False; listar pendentes mostra só id 2."""
        with tempfile.TemporaryDirectory() as pasta:
            repo = p.RepositorioTarefas(Path(pasta) / "tarefas.sqlite3")
            repo.adicionar("A")
            repo.adicionar("B")
            self.assertValor(repo.concluir(1), True)
            self.assertValor(repo.concluir(1), True)
            self.assertValor(repo.concluir(99), False)
            self.assertValor(repo.listar(), [{"id": 1, "titulo": "A", "concluida": True}, {"id": 2, "titulo": "B", "concluida": False}])
            self.assertValor(repo.listar(pendentes=True), [{"id": 2, "titulo": "B", "concluida": False}])

    def test_A32_04(self):
        r"""A32-04: Outra instância recupera título com apóstrofo e situação concluída; arquivo possui cabeçalho SQLite."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "tarefas.sqlite3"
            repo = p.RepositorioTarefas(caminho)
            titulo = "Ler D'Ávila; --"
            repo.adicionar(titulo)
            repo.concluir(1)
            outra = p.RepositorioTarefas(str(caminho))
            self.assertValor(outra.listar(), [{"id": 1, "titulo": titulo, "concluida": True}])
            self.assertTrue(caminho.read_bytes().startswith(b"SQLite format 3\x00"))

    def test_A32_05(self):
        r"""A32-05: CLI: adicionar, listar, concluir e listar --pendentes produzem as mensagens exatas e códigos 0."""
        with tempfile.TemporaryDirectory() as pasta:
            base = ["--banco", str(Path(pasta) / "tarefas.sqlite3")]
            casos = [(["adicionar", " Ler "], "Criada: 1\n"), (["listar"], "1 | [ ] | Ler\n"), (["concluir", "1"], "Concluída: 1\n"), (["listar"], "1 | [x] | Ler\n"), (["listar", "--pendentes"], "Nenhuma tarefa.\n")]
            for argumentos, esperado in casos:
                with redirect_stdout(io.StringIO()) as saida, redirect_stderr(io.StringIO()) as erros:
                    self.assertValor(p.main(base + argumentos), 0)
                self.assertEqual(saida.getvalue(), esperado)
                self.assertEqual(erros.getvalue(), "")

    def test_A32_06(self):
        r"""A32-06: CLI título vazio e ID inexistente: código 1, stdout vazio, stderr com mensagem exata."""
        with tempfile.TemporaryDirectory() as pasta:
            base = ["--banco", str(Path(pasta) / "tarefas.sqlite3")]
            for argumentos, mensagem in [(["adicionar", " "], "Erro: título inválido.\n"), (["concluir", "99"], "Erro: tarefa não encontrada.\n")]:
                with redirect_stdout(io.StringIO()) as saida, redirect_stderr(io.StringIO()) as erros:
                    self.assertValor(p.main(base + argumentos), 1)
                self.assertEqual(saida.getvalue(), "")
                self.assertEqual(erros.getvalue(), mensagem)

    def test_A32_07(self):
        r"""A32-07: CLI comando ausente, desconhecido ou ID não inteiro: SystemExit 2; --help: SystemExit 0 sem criar banco."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "tarefas.sqlite3"
            base = ["--banco", str(caminho)]
            for argumentos in [[], ["outro"], ["concluir", "x"]]:
                with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as erro:
                    p.main(base + argumentos)
                self.assertEqual(erro.exception.code, 2)
            with redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as erro:
                p.main(base + ["--help"])
            self.assertEqual(erro.exception.code, 0)
            self.assertFalse(caminho.exists())

    def test_A32_08(self):
        r"""A32-08: Execuções reais em processos distintos: adicionar 'Persistência' e listar recupera id 1 pendente."""
        with tempfile.TemporaryDirectory() as pasta:
            comando = [sys.executable, "-m", "praticas.aula32_projeto_final.pratica", "--banco", str(Path(pasta) / "tarefas.sqlite3")]
            ambiente = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
            primeiro = subprocess.run(comando + ["adicionar", "Persistência"], cwd=ROOT, env=ambiente, capture_output=True, text=True, encoding="utf-8", timeout=10)
            segundo = subprocess.run(comando + ["listar"], cwd=ROOT, env=ambiente, capture_output=True, text=True, encoding="utf-8", timeout=10)
            self.assertEqual(primeiro.returncode, 0, primeiro.stderr)
            self.assertEqual(primeiro.stdout, "Criada: 1\n")
            self.assertEqual(segundo.returncode, 0, segundo.stderr)
            self.assertEqual(segundo.stdout, "1 | [ ] | Persistência\n")


if __name__ == "__main__":
    unittest.main()

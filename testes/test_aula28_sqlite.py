"""Casos públicos da aula 28. Cada A28-NN está descrito em PRATICA.md."""

import unittest
from pathlib import Path
import sqlite3
import tempfile
from contextlib import closing
from testes.apoio import Contrato

from praticas.aula28_sqlite import pratica as p


class TestAula28(Contrato):

    def test_A28_01(self):
        r"""A28-01: Tabela recém-criada lista []; inserir ' Estudar ' retorna id 1 e lista [(1, 'Estudar')]."""
        with closing(sqlite3.connect(":memory:")) as conexao:
            self.assertIsNone(p.criar_tabela(conexao))
            self.assertValor(p.listar_tarefas(conexao), [])
            self.assertValor(p.adicionar_tarefa(conexao, " Estudar "), 1)
            self.assertValor(p.listar_tarefas(conexao), [(1, "Estudar")])

    def test_A28_02(self):
        r"""A28-02: Duas inclusões obtêm IDs 1 e 2; chamar criar_tabela de novo preserva ambas na ordem."""
        with closing(sqlite3.connect(":memory:")) as conexao:
            p.criar_tabela(conexao)
            self.assertValor(p.adicionar_tarefa(conexao, "B"), 1)
            self.assertValor(p.adicionar_tarefa(conexao, "A"), 2)
            p.criar_tabela(conexao)
            self.assertValor(p.listar_tarefas(conexao), [(1, "B"), (2, "A")])

    def test_A28_03(self):
        r"""A28-03: Título com apóstrofo e SQL aparente é armazenado literalmente e a tabela continua existindo."""
        with closing(sqlite3.connect(":memory:")) as conexao:
            p.criar_tabela(conexao)
            titulo = "D'Ávila'); DROP TABLE tarefas; --"
            p.adicionar_tarefa(conexao, titulo)
            self.assertValor(p.listar_tarefas(conexao), [(1, titulo)])

    def test_A28_04(self):
        r"""A28-04: Títulos '' e '   ' → ValueError: título vazio; não inserem linhas."""
        with closing(sqlite3.connect(":memory:")) as conexao:
            p.criar_tabela(conexao)
            for titulo in ["", "   "]:
                with self.assertRaises(ValueError) as erro:
                    p.adicionar_tarefa(conexao, titulo)
                self.assertEqual(str(erro.exception), "título vazio")
            self.assertValor(p.listar_tarefas(conexao), [])

    def test_A28_05(self):
        r"""A28-05: Inclusão em arquivo é visível por uma segunda conexão após fechar a primeira."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "tarefas.sqlite3"
            with closing(sqlite3.connect(caminho)) as conexao:
                p.criar_tabela(conexao)
                p.adicionar_tarefa(conexao, "Persistiu")
            with closing(sqlite3.connect(caminho)) as outra:
                self.assertValor(p.listar_tarefas(outra), [(1, "Persistiu")])


if __name__ == "__main__":
    unittest.main()

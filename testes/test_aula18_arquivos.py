"""Casos públicos da aula 18. Cada A18-NN está descrito em PRATICA.md."""

import unittest
from pathlib import Path
import tempfile
from testes.apoio import Contrato

from praticas.aula18_arquivos import pratica as p


class TestAula18(Contrato):

    def test_A18_01(self):
        r"""A18-01: Salvar ['Olá', '', ' fim '] escreve exatamente 'Olá\n\n fim \n' em UTF-8, preserva lista e retorna None."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "texto.txt"
            linhas = ["Olá", "", " fim "]
            self.assertIsNone(p.salvar_linhas(caminho, linhas))
            self.assertEqual(caminho.read_bytes(), "Olá\n\n fim \n".encode("utf-8"))
            self.assertValor(linhas, ["Olá", "", " fim "])

    def test_A18_02(self):
        r"""A18-02: Salvar [] usando caminho str apaga conteúdo antigo e deixa arquivo vazio."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "texto.txt"
            caminho.write_text("antigo", encoding="utf-8")
            self.assertIsNone(p.salvar_linhas(str(caminho), []))
            self.assertEqual(caminho.read_bytes(), b"")

    def test_A18_03(self):
        r"""A18-03: Ler 'Olá\n\n fim \n' e a variante sem quebra final → ['Olá', '', ' fim ']."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "texto.txt"
            for texto in ["Olá\n\n fim \n", "Olá\n\n fim "]:
                caminho.write_bytes(texto.encode("utf-8"))
                self.assertValor(p.ler_linhas(str(caminho)), ["Olá", "", " fim "])

    def test_A18_04(self):
        r"""A18-04: Ler arquivo ausente e arquivo vazio → []; ausência não cria arquivo."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "texto.txt"
            self.assertValor(p.ler_linhas(caminho), [])
            self.assertFalse(caminho.exists())
            caminho.write_bytes(b"")
            self.assertValor(p.ler_linhas(caminho), [])


if __name__ == "__main__":
    unittest.main()

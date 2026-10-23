"""Casos públicos da aula 03. Cada A03-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula03_tipos_conversoes import pratica as p


class TestAula03(Contrato):

    def test_A03_01(self):
        r"""A03-01: dobrar('12') → inteiro 24."""
        self.assertValor(p.dobrar("12"), 24)

    def test_A03_02(self):
        r"""A03-02: dobrar(' -3 ') → inteiro -6."""
        self.assertValor(p.dobrar(" -3 "), -6)

    def test_A03_03(self):
        r"""A03-03: dobrar('0') → inteiro 0."""
        self.assertValor(p.dobrar("0"), 0)

    def test_A03_04(self):
        r"""A03-04: eh_python('Python') → True."""
        self.assertValor(p.eh_python("Python"), True)

    def test_A03_05(self):
        r"""A03-05: eh_python('python'), eh_python(' Python') e eh_python('') → False."""
        for texto in ["python", " Python", ""]:
            self.assertValor(p.eh_python(texto), False)


if __name__ == "__main__":
    unittest.main()

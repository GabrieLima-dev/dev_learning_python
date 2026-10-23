"""Casos públicos da aula 02. Cada A02-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula02_git import pratica as p


class TestAula02(Contrato):

    def test_A02_01(self):
        r"""A02-01: COMANDO_ESTADO é `'git status'`."""
        self.assertValor(p.COMANDO_ESTADO, "git status")

    def test_A02_02(self):
        r"""A02-02: COMANDO_DIFERENCAS é `'git diff'`."""
        self.assertValor(p.COMANDO_DIFERENCAS, "git diff")

    def test_A02_03(self):
        r"""A02-03: COMANDO_PREPARADO é `'git diff --staged'`."""
        self.assertValor(p.COMANDO_PREPARADO, "git diff --staged")

    def test_A02_04(self):
        r"""A02-04: PASTA_LOCAL é `'.learning/'`."""
        self.assertValor(p.PASTA_LOCAL, ".learning/")


if __name__ == "__main__":
    unittest.main()

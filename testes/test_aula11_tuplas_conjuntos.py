"""Casos públicos da aula 11. Cada A11-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula11_tuplas_conjuntos import pratica as p


class TestAula11(Contrato):

    def test_A11_01(self):
        r"""A11-01: coordenadas('2,3') → tupla (2.0, 3.0)."""
        self.assertValor(p.coordenadas("2,3"), (2.0, 3.0))

    def test_A11_02(self):
        r"""A11-02: coordenadas(' -2.5, 0 ') → (-2.5, 0.0)."""
        self.assertValor(p.coordenadas(" -2.5, 0 "), (-2.5, 0.0))

    def test_A11_03(self):
        r"""A11-03: comuns([3, 1, 3, 2], [3, 2, 2]) → [2, 3], sem mudar entradas."""
        a, b = [3, 1, 3, 2], [3, 2, 2]
        self.assertValor(p.comuns(a, b), [2, 3])
        self.assertValor(a, [3, 1, 3, 2])
        self.assertValor(b, [3, 2, 2])

    def test_A11_04(self):
        r"""A11-04: comuns([], [1]) e comuns([1], [2]) → []."""
        self.assertValor(p.comuns([], [1]), [])
        self.assertValor(p.comuns([1], [2]), [])

    def test_A11_05(self):
        r"""A11-05: comuns([-1, 0, -1], [0, -1]) → [-1, 0]."""
        self.assertValor(p.comuns([-1, 0, -1], [0, -1]), [-1, 0])


if __name__ == "__main__":
    unittest.main()

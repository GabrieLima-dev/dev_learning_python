"""Casos públicos da aula 09. Cada A09-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula09_listas import pratica as p


class TestAula09(Contrato):

    def test_A09_01(self):
        r"""A09-01: [-2, 3, 0, 3, 1] → positivos [3, 3, 1]; entrada preservada e resultado novo."""
        valores = [-2, 3, 0, 3, 1]
        resultado = p.selecionar_positivos(valores)
        self.assertValor(resultado, [3, 3, 1])
        self.assertValor(valores, [-2, 3, 0, 3, 1])
        self.assertIsNot(resultado, valores)

    def test_A09_02(self):
        r"""A09-02: Positivos de [] e de [-1, 0] → novas listas vazias."""
        for valores in [[], [-1, 0]]:
            resultado = p.selecionar_positivos(valores)
            self.assertValor(resultado, [])
            self.assertIsNot(resultado, valores)

    def test_A09_03(self):
        r"""A09-03: Rotação de [1, 2, 3] → [3, 1, 2]; entrada preservada."""
        valores = [1, 2, 3]
        resultado = p.rotacionar(valores)
        self.assertValor(resultado, [3, 1, 2])
        self.assertValor(valores, [1, 2, 3])
        self.assertIsNot(resultado, valores)

    def test_A09_04(self):
        r"""A09-04: Rotação de [] e [8] → cópias com os mesmos valores."""
        for valores in [[], [8]]:
            resultado = p.rotacionar(valores)
            self.assertValor(resultado, valores)
            self.assertIsNot(resultado, valores)

    def test_A09_05(self):
        r"""A09-05: Rotação de [2, 2, 7, 2] → [2, 2, 2, 7]."""
        self.assertValor(p.rotacionar([2, 2, 7, 2]), [2, 2, 2, 7])


if __name__ == "__main__":
    unittest.main()

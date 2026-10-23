"""Casos públicos da aula 08. Cada A08-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula08_repeticoes import pratica as p


class TestAula08(Contrato):

    def test_A08_01(self):
        r"""A08-01: somar_ate(0) → 0; somar_ate(1) → 1."""
        self.assertValor(p.somar_ate(0), 0)
        self.assertValor(p.somar_ate(1), 1)

    def test_A08_02(self):
        r"""A08-02: somar_ate(5) → 15; somar_ate(100) → 5050."""
        self.assertValor(p.somar_ate(5), 15)
        self.assertValor(p.somar_ate(100), 5050)

    def test_A08_03(self):
        r"""A08-03: contar_pares(1, 6) → 3."""
        self.assertValor(p.contar_pares(1, 6), 3)

    def test_A08_04(self):
        r"""A08-04: contar_pares(-3, 2) → 3, contando -2, 0 e 2."""
        self.assertValor(p.contar_pares(-3, 2), 3)

    def test_A08_05(self):
        r"""A08-05: contar_pares(4, 4) → 1; (3, 3) → 0; (5, 2) → 0."""
        self.assertValor(p.contar_pares(4, 4), 1)
        self.assertValor(p.contar_pares(3, 3), 0)
        self.assertValor(p.contar_pares(5, 2), 0)


if __name__ == "__main__":
    unittest.main()

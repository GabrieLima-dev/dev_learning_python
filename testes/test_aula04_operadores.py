"""Casos públicos da aula 04. Cada A04-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula04_operadores import pratica as p


class TestAula04(Contrato):

    def test_A04_01(self):
        r"""A04-01: Pedido (1250, 3, 250) → 3500 centavos."""
        self.assertValor(p.total_pedido(1250, 3, 250), 3500)

    def test_A04_02(self):
        r"""A04-02: Pedido (0, 2, 0) e (100, 0, 0) → 0."""
        self.assertValor(p.total_pedido(0, 2, 0), 0)
        self.assertValor(p.total_pedido(100, 0, 0), 0)

    def test_A04_03(self):
        r"""A04-03: Pedido (900, 1, 900) → 0; (101, 2, 1) → 201."""
        self.assertValor(p.total_pedido(900, 1, 900), 0)
        self.assertValor(p.total_pedido(101, 2, 1), 201)

    def test_A04_04(self):
        r"""A04-04: 0 minutos → 0 horas e 0 restantes."""
        self.assertValor(p.horas_completas(0), 0)
        self.assertValor(p.minutos_restantes(0), 0)

    def test_A04_05(self):
        r"""A04-05: 59 minutos → 0 horas e 59 restantes."""
        self.assertValor(p.horas_completas(59), 0)
        self.assertValor(p.minutos_restantes(59), 59)

    def test_A04_06(self):
        r"""A04-06: 60 minutos → 1 hora e 0 restantes; 135 → 2 e 15."""
        self.assertValor(p.horas_completas(60), 1)
        self.assertValor(p.minutos_restantes(60), 0)
        self.assertValor(p.horas_completas(135), 2)
        self.assertValor(p.minutos_restantes(135), 15)


if __name__ == "__main__":
    unittest.main()

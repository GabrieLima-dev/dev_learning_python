"""Casos públicos da aula 16. Cada A16-NN está descrito em PRATICA.md."""

import unittest
from unittest.mock import patch, call
from testes.apoio import Contrato

from praticas.aula16_modulos import pratica as p


class TestAula16(Contrato):

    def test_A16_01(self):
        r"""A16-01: subtotal(125, 3) → 375; subtotal(100, 0) → 0."""
        self.assertValor(p.operacoes.subtotal(125, 3), 375)
        self.assertValor(p.operacoes.subtotal(100, 0), 0)

    def test_A16_02(self):
        r"""A16-02: total([(100, 2), (50, 3)]) → 350, entrada preservada."""
        itens = [(100, 2), (50, 3)]
        self.assertValor(p.total(itens), 350)
        self.assertValor(itens, [(100, 2), (50, 3)])

    def test_A16_03(self):
        r"""A16-03: total([]) → 0."""
        self.assertValor(p.total([]), 0)

    def test_A16_04(self):
        r"""A16-04: Delegação: subtotal simulado devolve 11 e 22; total retorna 33 e chama com (100, 2), depois (50, 3)."""
        with patch.object(p.operacoes, "subtotal", side_effect=[11, 22]) as subtotal:
            self.assertValor(p.total([(100, 2), (50, 3)]), 33)
        self.assertEqual(subtotal.call_args_list, [call(100, 2), call(50, 3)])


if __name__ == "__main__":
    unittest.main()

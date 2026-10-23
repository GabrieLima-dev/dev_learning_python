"""Casos públicos da aula 12. Cada A12-NN está descrito em PRATICA.md."""

import unittest
import copy
from testes.apoio import Contrato

from praticas.aula12_dicionarios import pratica as p


class TestAula12(Contrato):

    def test_A12_01(self):
        r"""A12-01: ['Ana', 'Bia', 'Ana', 'ana'] → {'Ana': 2, 'Bia': 1, 'ana': 1}."""
        votos = ["Ana", "Bia", "Ana", "ana"]
        self.assertValor(p.contar_votos(votos), {"Ana": 2, "Bia": 1, "ana": 1})
        self.assertValor(votos, ["Ana", "Bia", "Ana", "ana"])

    def test_A12_02(self):
        r"""A12-02: contar_votos([]) → {}."""
        self.assertValor(p.contar_votos([]), {})

    def test_A12_03(self):
        r"""A12-03: Estoque com (150, 2) e (900, 1) → 1200; preserva registros."""
        produtos = [{"preco_centavos": 150, "quantidade": 2}, {"preco_centavos": 900, "quantidade": 1}]
        antes = copy.deepcopy(produtos)
        self.assertValor(p.valor_estoque(produtos), 1200)
        self.assertValor(produtos, antes)

    def test_A12_04(self):
        r"""A12-04: Estoque vazio → 0; produto de preço 100 e quantidade 0 → 0."""
        self.assertValor(p.valor_estoque([]), 0)
        self.assertValor(p.valor_estoque([{"preco_centavos": 100, "quantidade": 0}]), 0)


if __name__ == "__main__":
    unittest.main()

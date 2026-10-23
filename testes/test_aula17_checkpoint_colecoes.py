"""Casos públicos da aula 17. Cada A17-NN está descrito em PRATICA.md."""

import unittest
import copy
from testes.apoio import Contrato

from praticas.aula17_checkpoint_colecoes import pratica as p


class TestAula17(Contrato):

    def test_A17_01(self):
        r"""A17-01: Entrada vazia → {}."""
        self.assertValor(p.resumir_vendas([]), {})

    def test_A17_02(self):
        r"""A17-02: Livro: 2×500 e 1×700; Caneta: 3×100 → Livro quantidade 3/receita 1700 e Caneta 3/300; preserva entrada."""
        vendas = [{"produto": "Livro", "quantidade": 2, "preco_centavos": 500}, {"produto": "Caneta", "quantidade": 3, "preco_centavos": 100}, {"produto": "Livro", "quantidade": 1, "preco_centavos": 700}]
        antes = copy.deepcopy(vendas)
        self.assertValor(p.resumir_vendas(vendas), {"Livro": {"quantidade": 3, "receita_centavos": 1700}, "Caneta": {"quantidade": 3, "receita_centavos": 300}})
        self.assertValor(vendas, antes)

    def test_A17_03(self):
        r"""A17-03: Produtos 'A' e 'a' são separados; preço zero é aceito."""
        self.assertValor(p.resumir_vendas([{"produto": "A", "quantidade": 1, "preco_centavos": 0}, {"produto": "a", "quantidade": 2, "preco_centavos": 10}]), {"A": {"quantidade": 1, "receita_centavos": 0}, "a": {"quantidade": 2, "receita_centavos": 20}})

    def test_A17_04(self):
        r"""A17-04: Quantidade 0, quantidade -1 ou preço -1 → ValueError: venda inválida; entrada permanece intacta mesmo após venda válida."""
        for quantidade, preco in [(0, 10), (-1, 10), (1, -1)]:
            vendas = [{"produto": "OK", "quantidade": 1, "preco_centavos": 10}, {"produto": "X", "quantidade": quantidade, "preco_centavos": preco}]
            antes = copy.deepcopy(vendas)
            with self.assertRaises(ValueError) as erro:
                p.resumir_vendas(vendas)
            self.assertEqual(str(erro.exception), "venda inválida")
            self.assertValor(vendas, antes)


if __name__ == "__main__":
    unittest.main()

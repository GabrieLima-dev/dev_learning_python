"""Casos públicos da aula 24. Cada A24-NN está descrito em PRATICA.md."""

import unittest
import dataclasses
from testes.apoio import Contrato

from praticas.aula24_composicao import pratica as p


class TestAula24(Contrato):

    def test_A24_01(self):
        r"""A24-01: Item('Livro', 500) tem quantidade 1 e subtotal 500; Item('Caneta', 100, 3) tem subtotal 300."""
        item = p.Item("Livro", 500)
        self.assertValor(item.nome, "Livro")
        self.assertValor(item.quantidade, 1)
        self.assertValor(item.subtotal(), 500)
        self.assertValor(p.Item("Caneta", 100, 3).subtotal(), 300)

    def test_A24_02(self):
        r"""A24-02: Item é dataclass, igualdade compara campos, e alterar quantidade levanta FrozenInstanceError."""
        item = p.Item("Livro", 500)
        self.assertTrue(dataclasses.is_dataclass(item))
        self.assertEqual(item, p.Item("Livro", 500))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            item.quantidade = 2

    def test_A24_03(self):
        r"""A24-03: Carrinho vazio → 0; adicionar Livro/500 e Caneta/100×3 → 800; adicionar Livro novamente → 1300."""
        carrinho = p.Carrinho()
        self.assertValor(carrinho.total(), 0)
        livro = p.Item("Livro", 500)
        self.assertIsNone(carrinho.adicionar(livro))
        carrinho.adicionar(p.Item("Caneta", 100, 3))
        self.assertValor(carrinho.total(), 800)
        carrinho.adicionar(livro)
        self.assertValor(carrinho.total(), 1300)

    def test_A24_04(self):
        r"""A24-04: Adicionar item de valor 10 a um carrinho mantém outro em 0."""
        a, b = p.Carrinho(), p.Carrinho()
        a.adicionar(p.Item("A", 10))
        self.assertValor(a.total(), 10)
        self.assertValor(b.total(), 0)


if __name__ == "__main__":
    unittest.main()

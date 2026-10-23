"""Casos públicos da aula 05. Cada A05-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula05_textos import pratica as p


class TestAula05(Contrato):

    def test_A05_01(self):
        r"""A05-01: normalizar_usuario('  ANA  ') → 'ana'."""
        self.assertValor(p.normalizar_usuario("  ANA  "), "ana")

    def test_A05_02(self):
        r"""A05-02: normalizar_usuario('  JOÃO SILVA ') → 'joão silva'."""
        self.assertValor(p.normalizar_usuario("  JOÃO SILVA "), "joão silva")

    def test_A05_03(self):
        r"""A05-03: String vazia e '   ' → ''."""
        self.assertValor(p.normalizar_usuario(""), "")
        self.assertValor(p.normalizar_usuario("   "), "")

    def test_A05_04(self):
        r"""A05-04: etiqueta('Livro', 2) → 'Item: Livro (2)'."""
        self.assertValor(p.etiqueta("Livro", 2), "Item: Livro (2)")

    def test_A05_05(self):
        r"""A05-05: etiqueta(' Chá ', 0) → 'Item:  Chá  (0)'; espaços do produto são preservados."""
        self.assertValor(p.etiqueta(" Chá ", 0), "Item:  Chá  (0)")


if __name__ == "__main__":
    unittest.main()

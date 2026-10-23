"""Casos públicos da aula 10. Cada A10-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula10_checkpoint_fundamentos import pratica as p


class TestAula10(Contrato):

    def test_A10_01(self):
        r"""A10-01: [] → 'Quantidade: 0 | Média: 0.00 | Aprovados: 0'."""
        self.assertValor(p.relatorio_notas([]), "Quantidade: 0 | Média: 0.00 | Aprovados: 0")

    def test_A10_02(self):
        r"""A10-02: [7] → 'Quantidade: 1 | Média: 7.00 | Aprovados: 1'."""
        self.assertValor(p.relatorio_notas([7]), "Quantidade: 1 | Média: 7.00 | Aprovados: 1")

    def test_A10_03(self):
        r"""A10-03: [10, 5, 7] → 'Quantidade: 3 | Média: 7.33 | Aprovados: 2'."""
        self.assertValor(p.relatorio_notas([10, 5, 7]), "Quantidade: 3 | Média: 7.33 | Aprovados: 2")

    def test_A10_04(self):
        r"""A10-04: [6.9, 7.1, 0] → 'Quantidade: 3 | Média: 4.67 | Aprovados: 1'; preserva entrada."""
        notas = [6.9, 7.1, 0]
        self.assertValor(p.relatorio_notas(notas), "Quantidade: 3 | Média: 4.67 | Aprovados: 1")
        self.assertValor(notas, [6.9, 7.1, 0])

    def test_A10_05(self):
        r"""A10-05: [0, 0] → 'Quantidade: 2 | Média: 0.00 | Aprovados: 0'."""
        self.assertValor(p.relatorio_notas([0, 0]), "Quantidade: 2 | Média: 0.00 | Aprovados: 0")


if __name__ == "__main__":
    unittest.main()

"""Casos públicos da aula 14. Cada A14-NN está descrito em PRATICA.md."""

import unittest
import copy
from testes.apoio import Contrato

from praticas.aula14_compreensoes_ordenacao import pratica as p


class TestAula14(Contrato):

    def test_A14_01(self):
        r"""A14-01: quadrados_pares([-2, 3, 0, 4, 4]) → [4, 0, 16, 16]."""
        valores = [-2, 3, 0, 4, 4]
        self.assertValor(p.quadrados_pares(valores), [4, 0, 16, 16])
        self.assertValor(valores, [-2, 3, 0, 4, 4])

    def test_A14_02(self):
        r"""A14-02: quadrados_pares([]) e quadrados_pares([1, 3]) → []."""
        self.assertValor(p.quadrados_pares([]), [])
        self.assertValor(p.quadrados_pares([1, 3]), [])

    def test_A14_03(self):
        r"""A14-03: Bia 8, Ana 8, Rui 10 → Rui 10, Ana 8, Bia 8; entrada preservada."""
        alunos = [{"nome": "Bia", "nota": 8}, {"nome": "Ana", "nota": 8}, {"nome": "Rui", "nota": 10}]
        antes = copy.deepcopy(alunos)
        resultado = p.ordenar_alunos(alunos)
        self.assertValor(resultado, [alunos[2], alunos[1], alunos[0]])
        self.assertValor(alunos, antes)
        self.assertIsNot(resultado, alunos)

    def test_A14_04(self):
        r"""A14-04: ordenar_alunos([]) → uma nova lista vazia."""
        alunos = []
        resultado = p.ordenar_alunos(alunos)
        self.assertValor(resultado, [])
        self.assertIsNot(resultado, alunos)


if __name__ == "__main__":
    unittest.main()

"""Casos públicos da aula 26. Cada A26-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula26_geradores import pratica as p


class TestAula26(Contrato):

    def test_A26_01(self):
        r"""A26-01: pares_ate(5) é iterador, produz [0, 2, 4] e depois []; limite 0 → [0], limite 6 → [0, 2, 4, 6]."""
        resultado = p.pares_ate(5)
        self.assertIs(iter(resultado), resultado)
        self.assertValor(list(resultado), [0, 2, 4])
        self.assertValor(list(resultado), [])
        self.assertValor(list(p.pares_ate(0)), [0])
        self.assertValor(list(p.pares_ate(6)), [0, 2, 4, 6])

    def test_A26_02(self):
        r"""A26-02: lotes(iter([1, 2, 3, 4, 5]), 2) → [[1, 2], [3, 4], [5]]; listas independentes."""
        resultado = p.lotes(iter([1, 2, 3, 4, 5]), 2)
        self.assertIs(iter(resultado), resultado)
        lotes = list(resultado)
        self.assertValor(lotes, [[1, 2], [3, 4], [5]])
        lotes[0].append(99)
        self.assertValor(lotes[1], [3, 4])

    def test_A26_03(self):
        r"""A26-03: lotes([], 2) → []; lotes([1, 2], 1) → [[1], [2]]."""
        self.assertValor(list(p.lotes([], 2)), [])
        self.assertValor(list(p.lotes([1, 2], 1)), [[1], [2]])

    def test_A26_04(self):
        r"""A26-04: Tamanhos 0 e -1 → ValueError: tamanho deve ser positivo."""
        for tamanho in [0, -1]:
            with self.assertRaises(ValueError) as erro:
                list(p.lotes([], tamanho))
            self.assertEqual(str(erro.exception), "tamanho deve ser positivo")

    def test_A26_05(self):
        r"""A26-05: Criar lotes não consome entrada; pedir primeiro lote de 2 consome exatamente [10, 20], sem buscar terceiro."""
        consumidos = []
        def origem():
            for valor in [10, 20]:
                consumidos.append(valor)
                yield valor
            raise AssertionError("Não deveria consumir o terceiro item ainda")
        resultado = p.lotes(origem(), 2)
        self.assertEqual(consumidos, [])
        self.assertValor(next(resultado), [10, 20])
        self.assertEqual(consumidos, [10, 20])


if __name__ == "__main__":
    unittest.main()

"""Casos públicos da aula 15. Cada A15-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula15_excecoes import pratica as p


class TestAula15(Contrato):

    def test_A15_01(self):
        r"""A15-01: dividir(7, 2) → 3.5; dividir(-4, 2) → -2.0."""
        self.assertValor(p.dividir(7, 2), 3.5)
        self.assertValor(p.dividir(-4, 2), -2.0)

    def test_A15_02(self):
        r"""A15-02: dividir(1, 0) e dividir(0, 0) → ValueError: divisor não pode ser zero."""
        for a in [1, 0]:
            with self.assertRaises(ValueError) as erro:
                p.dividir(a, 0)
            self.assertEqual(str(erro.exception), "divisor não pode ser zero")

    def test_A15_03(self):
        r"""A15-03: ler_idade(' 18 '), '0' e '130' → 18, 0 e 130."""
        for texto, esperado in [(" 18 ", 18), ("0", 0), ("130", 130)]:
            self.assertValor(p.ler_idade(texto), esperado)

    def test_A15_04(self):
        r"""A15-04: Idades '', 'abc', '2.5', '-1' e '131' → ValueError: idade inválida."""
        for texto in ["", "abc", "2.5", "-1", "131"]:
            with self.assertRaises(ValueError) as erro:
                p.ler_idade(texto)
            self.assertEqual(str(erro.exception), "idade inválida")


if __name__ == "__main__":
    unittest.main()

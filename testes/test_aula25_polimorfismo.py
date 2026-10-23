"""Casos públicos da aula 25. Cada A25-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula25_polimorfismo import pratica as p


class TestAula25(Contrato):

    def test_A25_01(self):
        r"""A25-01: Forma().area() levanta NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            p.Forma().area()

    def test_A25_02(self):
        r"""A25-02: Retangulo(3, 4).area() → 12 e Retangulo(0, 5) → 0; herda de Forma."""
        retangulo = p.Retangulo(3, 4)
        self.assertIsInstance(retangulo, p.Forma)
        self.assertEqual(retangulo.area(), 12)
        self.assertEqual(p.Retangulo(0, 5).area(), 0)

    def test_A25_03(self):
        r"""A25-03: Quadrado(2.5).area() → 6.25 e é Retangulo."""
        quadrado = p.Quadrado(2.5)
        self.assertIsInstance(quadrado, p.Retangulo)
        self.assertEqual(quadrado.area(), 6.25)

    def test_A25_04(self):
        r"""A25-04: Total de Retangulo(3, 4) e Quadrado(2) → 16; vazio → 0."""
        self.assertEqual(p.total_areas([p.Retangulo(3, 4), p.Quadrado(2)]), 16)
        self.assertEqual(p.total_areas([]), 0)

    def test_A25_05(self):
        r"""A25-05: Um iterador de objetos externos que oferecem area() retornando 7 → total 14."""
        class Externa:
            def area(self):
                return 7
        self.assertEqual(p.total_areas(iter([Externa(), Externa()])), 14)


if __name__ == "__main__":
    unittest.main()

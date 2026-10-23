"""Casos públicos da aula 21. Cada A21-NN está descrito em PRATICA.md."""

import unittest
from decimal import Decimal
from testes.apoio import Contrato

from praticas.aula21_datas_decimal import pratica as p


class TestAula21(Contrato):

    def test_A21_01(self):
        r"""A21-01: 2024-02-28 até 2024-03-01 → 2 dias; 2023 no mesmo intervalo → 1."""
        self.assertValor(p.dias_entre("2024-02-28", "2024-03-01"), 2)
        self.assertValor(p.dias_entre("2023-02-28", "2023-03-01"), 1)

    def test_A21_02(self):
        r"""A21-02: 2025-01-01 até a mesma data → 0; 2025-01-03 até 2025-01-01 → -2."""
        self.assertValor(p.dias_entre("2025-01-01", "2025-01-01"), 0)
        self.assertValor(p.dias_entre("2025-01-03", "2025-01-01"), -2)

    def test_A21_03(self):
        r"""A21-03: ['0.10', '0.20'] → Decimal('0.30') com duas casas; preserva lista."""
        textos = ["0.10", "0.20"]
        resultado = p.somar_precos(textos)
        self.assertValor(resultado, Decimal("0.30"))
        self.assertEqual(resultado.as_tuple().exponent, -2)
        self.assertValor(textos, ["0.10", "0.20"])

    def test_A21_04(self):
        r"""A21-04: ['0.005', '0.005'] → Decimal('0.01'), arredondando apenas a soma."""
        self.assertValor(p.somar_precos(["0.005", "0.005"]), Decimal("0.01"))

    def test_A21_05(self):
        r"""A21-05: ['-1.005'] → Decimal('-1.01'); [] → Decimal('0.00') com duas casas."""
        self.assertValor(p.somar_precos(["-1.005"]), Decimal("-1.01"))
        resultado = p.somar_precos([])
        self.assertValor(resultado, Decimal("0.00"))
        self.assertEqual(resultado.as_tuple().exponent, -2)


if __name__ == "__main__":
    unittest.main()

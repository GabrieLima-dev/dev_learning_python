"""Casos públicos da aula 13. Cada A13-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula13_funcoes import pratica as p


class TestAula13(Contrato):

    def test_A13_01(self):
        r"""A13-01: aplicar_desconto(1000) → 900; (101) → 90."""
        self.assertValor(p.aplicar_desconto(1000), 900)
        self.assertValor(p.aplicar_desconto(101), 90)

    def test_A13_02(self):
        r"""A13-02: aplicar_desconto(250, percentual=0) → 250; percentual=100 → 0."""
        self.assertValor(p.aplicar_desconto(250, percentual=0), 250)
        self.assertValor(p.aplicar_desconto(250, percentual=100), 0)

    def test_A13_03(self):
        r"""A13-03: aplicar_desconto(999, 25) → 749; valor zero → 0."""
        self.assertValor(p.aplicar_desconto(999, 25), 749)
        self.assertValor(p.aplicar_desconto(0), 0)

    def test_A13_04(self):
        r"""A13-04: total_com_desconto([101, 101]) → 181, com entrada preservada."""
        precos = [101, 101]
        self.assertValor(p.total_com_desconto(precos), 181)
        self.assertValor(precos, [101, 101])

    def test_A13_05(self):
        r"""A13-05: total_com_desconto([], percentual=30) → 0; [200, 300] com 20% → 400."""
        self.assertValor(p.total_com_desconto([], percentual=30), 0)
        self.assertValor(p.total_com_desconto([200, 300], percentual=20), 400)


if __name__ == "__main__":
    unittest.main()

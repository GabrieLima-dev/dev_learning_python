"""Casos públicos da aula 07. Cada A07-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula07_decisoes import pratica as p


class TestAula07(Contrato):

    def test_A07_01(self):
        r"""A07-01: Notas 0 e 4.99 → 'reprovado'."""
        for nota in [0, 4.99]:
            self.assertValor(p.classificar_nota(nota), "reprovado")

    def test_A07_02(self):
        r"""A07-02: Notas 5 e 6.99 → 'recuperacao'."""
        for nota in [5, 6.99]:
            self.assertValor(p.classificar_nota(nota), "recuperacao")

    def test_A07_03(self):
        r"""A07-03: Notas 7 e 10 → 'aprovado'."""
        for nota in [7, 10]:
            self.assertValor(p.classificar_nota(nota), "aprovado")

    def test_A07_04(self):
        r"""A07-04: Idade 11, com ou sem acompanhante → False."""
        self.assertValor(p.pode_entrar(11, True), False)
        self.assertValor(p.pode_entrar(11, False), False)

    def test_A07_05(self):
        r"""A07-05: Idades 12 e 17: acompanhado → True; sozinho → False."""
        for idade in [12, 17]:
            self.assertValor(p.pode_entrar(idade, True), True)
            self.assertValor(p.pode_entrar(idade, False), False)

    def test_A07_06(self):
        r"""A07-06: Idades 18 e 80, com ou sem acompanhante → True."""
        for idade in [18, 80]:
            for acompanhado in [True, False]:
                self.assertValor(p.pode_entrar(idade, acompanhado), True)


if __name__ == "__main__":
    unittest.main()

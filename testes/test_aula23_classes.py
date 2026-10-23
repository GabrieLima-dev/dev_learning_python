"""Casos públicos da aula 23. Cada A23-NN está descrito em PRATICA.md."""

import unittest
from testes.apoio import Contrato

from praticas.aula23_classes import pratica as p


class TestAula23(Contrato):

    def test_A23_01(self):
        r"""A23-01: Conta('Ana') começa com titular Ana e saldo 0; Conta('Bia', 500) começa com 500."""
        ana, bia = p.Conta("Ana"), p.Conta("Bia", 500)
        self.assertValor(ana.titular, "Ana")
        self.assertValor(ana.saldo, 0)
        self.assertValor(bia.saldo, 500)

    def test_A23_02(self):
        r"""A23-02: Saldo inicial -1 → ValueError: saldo inválido."""
        with self.assertRaises(ValueError) as erro:
            p.Conta("Ana", -1)
        self.assertEqual(str(erro.exception), "saldo inválido")

    def test_A23_03(self):
        r"""A23-03: Saldo 100, depositar 50 → 150; sacar 70 → 80; sacar 80 → 0."""
        conta = p.Conta("Ana", 100)
        self.assertValor(conta.depositar(50), 150)
        self.assertValor(conta.sacar(70), 80)
        self.assertValor(conta.sacar(80), 0)
        self.assertValor(conta.saldo, 0)

    def test_A23_04(self):
        r"""A23-04: Depósito e saque de 0 ou -1 → ValueError: valor deve ser positivo; saldo 100 preservado."""
        conta = p.Conta("Ana", 100)
        for metodo in [conta.depositar, conta.sacar]:
            for valor in [0, -1]:
                with self.assertRaises(ValueError) as erro:
                    metodo(valor)
                self.assertEqual(str(erro.exception), "valor deve ser positivo")
                self.assertValor(conta.saldo, 100)

    def test_A23_05(self):
        r"""A23-05: Sacar 101 de saldo 100 → ValueError: saldo insuficiente, sem alterar."""
        conta = p.Conta("Ana", 100)
        with self.assertRaises(ValueError) as erro:
            conta.sacar(101)
        self.assertEqual(str(erro.exception), "saldo insuficiente")
        self.assertValor(conta.saldo, 100)

    def test_A23_06(self):
        r"""A23-06: Depositar 50 na primeira de duas contas zeradas não modifica a segunda."""
        a, b = p.Conta("A"), p.Conta("B")
        a.depositar(50)
        self.assertValor(a.saldo, 50)
        self.assertValor(b.saldo, 0)


if __name__ == "__main__":
    unittest.main()

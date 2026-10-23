"""Casos públicos da aula 27. Cada A27-NN está descrito em PRATICA.md."""

import importlib
import unittest
from unittest.mock import patch
from testes.apoio import Contrato

from praticas.aula27_testes_debugging import pratica as p


class TestAula27(Contrato):

    def test_A27_01(self):
        r"""A27-01: Função corrigida: -1 gera ValueError exato; 0 e 19999 → 1200; 20000 e 30000 → 0."""
        with self.assertRaises(ValueError) as erro:
            p.frete(-1)
        self.assertEqual(str(erro.exception), "total inválido")
        for entrada, esperado in [(0, 1200), (19999, 1200), (20000, 0), (30000, 0)]:
            self.assertValor(p.frete(entrada), esperado)

    def test_A27_02(self):
        r"""A27-02: Sua classe TestFrete possui pelo menos quatro testes e todos passam na função corrigida."""
        modulo = importlib.import_module("praticas.aula27_testes_debugging.test_pratica")
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(modulo.TestFrete)
        self.assertGreaterEqual(suite.countTestCases(), 4, "Escreva pelo menos quatro métodos test_")
        resultado = unittest.TestResult()
        suite.run(resultado)
        self.assertTrue(resultado.wasSuccessful(), str(resultado.errors + resultado.failures))
        self.assertFalse(resultado.skipped, "Não pule seus testes")

    def test_A27_03(self):
        r"""A27-03: Seus testes rejeitam quatro funções defeituosas públicas: sempre 0, sempre 1200, limite >20000 e negativo aceito."""
        modulo = importlib.import_module("praticas.aula27_testes_debugging.test_pratica")
        def limite_errado(valor):
            if valor < 0:
                raise ValueError("total inválido")
            return 0 if valor > 20000 else 1200
        mutantes = [("sempre zero", lambda valor: 0), ("sempre 1200", lambda valor: 1200), ("limite errado", limite_errado), ("negativo aceito", lambda valor: 0 if valor >= 20000 else 1200)]
        for nome, mutante in mutantes:
            with self.subTest(mutante=nome), patch.object(p, "frete", mutante):
                suite = unittest.defaultTestLoader.loadTestsFromTestCase(modulo.TestFrete)
                resultado = unittest.TestResult()
                suite.run(resultado)
                self.assertFalse(resultado.wasSuccessful(), f"Seus testes aceitaram a regressão: {nome}")


if __name__ == "__main__":
    unittest.main()

"""Casos públicos da aula 06. Cada A06-NN está descrito em PRATICA.md."""

import unittest
import io
from contextlib import redirect_stdout
from unittest.mock import patch, call
from testes.apoio import Contrato

from praticas.aula06_entrada_saida import pratica as p


class TestAula06(Contrato):

    def test_A06_01(self):
        r"""A06-01: Entrada ' Ana ' → saída 'Olá, Ana!\n', uma leitura sem argumento e retorno None."""
        with patch("builtins.input", return_value=" Ana ") as entrada, redirect_stdout(io.StringIO()) as saida:
            self.assertIsNone(p.cumprimentar())
        entrada.assert_called_once_with()
        self.assertEqual(saida.getvalue(), "Olá, Ana!\n")

    def test_A06_02(self):
        r"""A06-02: Entrada vazia → saída 'Olá, !\n'."""
        with patch("builtins.input", return_value=""), redirect_stdout(io.StringIO()) as saida:
            self.assertIsNone(p.cumprimentar())
        self.assertEqual(saida.getvalue(), "Olá, !\n")

    def test_A06_03(self):
        r"""A06-03: Entradas '2' e '3' → saída '5\n', exatamente duas leituras sem argumentos."""
        with patch("builtins.input", side_effect=["2", "3"]) as entrada, redirect_stdout(io.StringIO()) as saida:
            self.assertIsNone(p.somar_entradas())
        self.assertEqual(entrada.call_args_list, [call(), call()])
        self.assertEqual(saida.getvalue(), "5\n")

    def test_A06_04(self):
        r"""A06-04: Entradas ' -4 ' e '4' → saída '0\n'."""
        with patch("builtins.input", side_effect=[" -4 ", "4"]), redirect_stdout(io.StringIO()) as saida:
            self.assertIsNone(p.somar_entradas())
        self.assertEqual(saida.getvalue(), "0\n")


if __name__ == "__main__":
    unittest.main()

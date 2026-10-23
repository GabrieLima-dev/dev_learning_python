"""Casos públicos da aula 31. Cada A31-NN está descrito em PRATICA.md."""

import unittest
import argparse
import io
from contextlib import redirect_stdout, redirect_stderr
from testes.apoio import Contrato

from praticas.aula31_linha_comando import pratica as p


class TestAula31(Contrato):

    def test_A31_01(self):
        r"""A31-01: Parser interpreta ['somar', '2', '-3'] como operacao='somar', numeros=[2, -3]."""
        parser = p.criar_parser()
        self.assertIsInstance(parser, argparse.ArgumentParser)
        args = parser.parse_args(["somar", "2", "-3"])
        self.assertValor(args.operacao, "somar")
        self.assertValor(args.numeros, [2, -3])

    def test_A31_02(self):
        r"""A31-02: main(['somar', '2', '-3', '8']) → código 0, stdout '7\n' e stderr vazio."""
        with redirect_stdout(io.StringIO()) as saida, redirect_stderr(io.StringIO()) as erros:
            self.assertValor(p.main(["somar", "2", "-3", "8"]), 0)
        self.assertEqual(saida.getvalue(), "7\n")
        self.assertEqual(erros.getvalue(), "")

    def test_A31_03(self):
        r"""A31-03: main(['maior', '-8', '-2', '-5']) → 0 e stdout '-2\n'."""
        with redirect_stdout(io.StringIO()) as saida:
            self.assertValor(p.main(["maior", "-8", "-2", "-5"]), 0)
        self.assertEqual(saida.getvalue(), "-2\n")

    def test_A31_04(self):
        r"""A31-04: Sem números, operação 'outra' ou número 'x' → SystemExit(2), stderr não vazio."""
        for argv in [["somar"], ["outra", "1"], ["somar", "x"]]:
            with redirect_stderr(io.StringIO()) as erros, self.assertRaises(SystemExit) as saida:
                p.main(argv)
            self.assertEqual(saida.exception.code, 2)
            self.assertTrue(erros.getvalue())

    def test_A31_05(self):
        r"""A31-05: --help → SystemExit(0), ajuda em stdout."""
        with redirect_stdout(io.StringIO()) as texto, self.assertRaises(SystemExit) as saida:
            p.main(["--help"])
        self.assertEqual(saida.exception.code, 0)
        self.assertTrue(texto.getvalue())


if __name__ == "__main__":
    unittest.main()

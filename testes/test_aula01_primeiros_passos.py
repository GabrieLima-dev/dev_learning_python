"""Casos públicos da aula 01. Cada A01-NN está descrito em PRATICA.md."""

import unittest
import io
from contextlib import redirect_stdout
from testes.apoio import Contrato

from praticas.aula01_primeiros_passos import pratica as p


class TestAula01(Contrato):

    def test_A01_01(self):
        r"""A01-01: Devolve exatamente `'Minha jornada em Python começou!'` como string."""
        self.assertValor(p.mensagem_inicial(), "Minha jornada em Python começou!")

    def test_A01_02(self):
        r"""A01-02: Duas chamadas devolvem o mesmo texto e não escrevem no terminal."""
        with redirect_stdout(io.StringIO()) as saida:
            self.assertValor(p.mensagem_inicial(), "Minha jornada em Python começou!")
            self.assertValor(p.mensagem_inicial(), "Minha jornada em Python começou!")
        self.assertEqual(saida.getvalue(), "")


if __name__ == "__main__":
    unittest.main()

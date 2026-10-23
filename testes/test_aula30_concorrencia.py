"""Casos públicos da aula 30. Cada A30-NN está descrito em PRATICA.md."""

import unittest
import threading
from testes.apoio import Contrato

from praticas.aula30_concorrencia import pratica as p


class TestAula30(Contrato):

    def test_A30_01(self):
        r"""A30-01: Aplicar quadrado a [3, 1, 2] → [9, 1, 4], preservando entrada; vazio → []."""
        itens = [3, 1, 2]
        self.assertValor(p.executar_em_ordem(lambda x: x * x, itens), [9, 1, 4])
        self.assertValor(itens, [3, 1, 2])
        self.assertValor(p.executar_em_ordem(lambda x: x, []), [])

    def test_A30_02(self):
        r"""A30-02: Duas tarefas passam juntas por Barrier(2), uma chamada por item, e retornam [20, 10] na ordem de [2, 1]."""
        barreira = threading.Barrier(2, timeout=5)
        chamadas = []
        trava = threading.Lock()
        def tarefa(valor):
            with trava:
                chamadas.append(valor)
            barreira.wait()
            return valor * 10
        self.assertValor(p.executar_em_ordem(tarefa, [2, 1]), [20, 10])
        self.assertEqual(sorted(chamadas), [1, 2])

    def test_A30_03(self):
        r"""A30-03: Tarefa que levanta ValueError('falha de tarefa') faz a função propagar tipo e mensagem."""
        def falhar(valor):
            raise ValueError("falha de tarefa")
        with self.assertRaises(ValueError) as erro:
            p.executar_em_ordem(falhar, [1])
        self.assertEqual(str(erro.exception), "falha de tarefa")


if __name__ == "__main__":
    unittest.main()

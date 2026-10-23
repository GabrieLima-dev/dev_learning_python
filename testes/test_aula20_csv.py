"""Casos públicos da aula 20. Cada A20-NN está descrito em PRATICA.md."""

import unittest
import copy
import csv
from pathlib import Path
import tempfile
from testes.apoio import Contrato

from praticas.aula20_csv import pratica as p


class TestAula20(Contrato):

    def test_A20_01(self):
        r"""A20-01: Exporta 'Café, moído'/1200 e nome com aspas e quebra de linha/0; leitura CSV confirma cabeçalho, campos e preservação."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "produtos.csv"
            produtos = [{"nome": "Café, moído", "preco_centavos": 1200}, {"nome": 'Kit "A"\nnovo', "preco_centavos": 0}]
            antes = copy.deepcopy(produtos)
            self.assertIsNone(p.exportar_produtos(caminho, produtos))
            with caminho.open(encoding="utf-8", newline="") as arquivo:
                linhas = list(csv.reader(arquivo))
            self.assertEqual(linhas, [["nome", "preco_centavos"], ["Café, moído", "1200"], ['Kit "A"\nnovo', "0"]])
            self.assertValor(produtos, antes)

    def test_A20_02(self):
        r"""A20-02: Exportar [] substitui arquivo anterior e produz só o cabeçalho."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "produtos.csv"
            caminho.write_text("antigo", encoding="utf-8")
            self.assertIsNone(p.exportar_produtos(str(caminho), []))
            with caminho.open(encoding="utf-8", newline="") as arquivo:
                self.assertEqual(list(csv.reader(arquivo)), [["nome", "preco_centavos"]])

    def test_A20_03(self):
        r"""A20-03: Importa CSV escrito pelo teste com vírgula, aspas, quebra e acento; preços voltam como int."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "produtos.csv"
            with caminho.open("w", encoding="utf-8", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows([["nome", "preco_centavos"], ["Café, moído", 1200], ['Kit "A"\nnovo', 0]])
            self.assertValor(p.importar_produtos(str(caminho)), [{"nome": "Café, moído", "preco_centavos": 1200}, {"nome": 'Kit "A"\nnovo', "preco_centavos": 0}])

    def test_A20_04(self):
        r"""A20-04: Arquivo só com cabeçalho → []."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "produtos.csv"
            caminho.write_text("nome,preco_centavos\n", encoding="utf-8")
            self.assertValor(p.importar_produtos(caminho), [])


if __name__ == "__main__":
    unittest.main()

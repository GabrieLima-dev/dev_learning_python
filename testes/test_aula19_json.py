"""Casos públicos da aula 19. Cada A19-NN está descrito em PRATICA.md."""

import unittest
import copy
import json
from pathlib import Path
import tempfile
from testes.apoio import Contrato

from praticas.aula19_json import pratica as p


class TestAula19(Contrato):

    def test_A19_01(self):
        r"""A19-01: Salvar {'tema': 'claro', 'nome': 'João', 'avisos': True} preserva dados e substitui arquivo antigo por JSON equivalente."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "config.json"
            caminho.write_text("antigo", encoding="utf-8")
            dados = {"tema": "claro", "nome": "João", "avisos": True}
            antes = copy.deepcopy(dados)
            self.assertIsNone(p.salvar_config(str(caminho), dados))
            self.assertValor(json.loads(caminho.read_text(encoding="utf-8")), dados)
            self.assertValor(dados, antes)

    def test_A19_02(self):
        r"""A19-02: Carregar objeto {'n': 2, 'itens': [1, None]} devolve esse dict."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "config.json"
            caminho.write_text(json.dumps({"n": 2, "itens": [1, None]}), encoding="utf-8")
            self.assertValor(p.carregar_config(caminho), {"n": 2, "itens": [1, None]})

    def test_A19_03(self):
        r"""A19-03: Arquivo ausente → {}, sem criar arquivo."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "config.json"
            self.assertValor(p.carregar_config(caminho), {})
            self.assertFalse(caminho.exists())

    def test_A19_04(self):
        r"""A19-04: Conteúdo '{' → JSONDecodeError; arquivo é preservado."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "config.json"
            caminho.write_text("{", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                p.carregar_config(caminho)
            self.assertEqual(caminho.read_text(encoding="utf-8"), "{")

    def test_A19_05(self):
        r"""A19-05: JSON [], null e 3 → ValueError: configuração deve ser objeto."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "config.json"
            for texto in ["[]", "null", "3"]:
                caminho.write_text(texto, encoding="utf-8")
                with self.assertRaises(ValueError) as erro:
                    p.carregar_config(caminho)
                self.assertEqual(str(erro.exception), "configuração deve ser objeto")


if __name__ == "__main__":
    unittest.main()

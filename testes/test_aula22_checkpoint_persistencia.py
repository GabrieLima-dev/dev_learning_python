"""Casos públicos da aula 22. Cada A22-NN está descrito em PRATICA.md."""

import unittest
import json
from pathlib import Path
import tempfile
from testes.apoio import Contrato

from praticas.aula22_checkpoint_persistencia import pratica as p


class TestAula22(Contrato):

    def test_A22_01(self):
        r"""A22-01: Histórico ausente → [] sem criar arquivo."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "eventos.json"
            self.assertValor(p.listar_eventos(caminho), [])
            self.assertFalse(caminho.exists())

    def test_A22_02(self):
        r"""A22-02: Registrar {tipo:' estudo ', descricao:' Python '} retorna 1; segundo evento retorna 2; preserva entrada e ordem no JSON."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "eventos.json"
            evento = {"tipo": " estudo ", "descricao": " Python "}
            self.assertValor(p.registrar_evento(caminho, evento), 1)
            self.assertValor(p.registrar_evento(str(caminho), {"tipo": "pausa", "descricao": "Café"}), 2)
            esperado = [{"tipo": "estudo", "descricao": "Python"}, {"tipo": "pausa", "descricao": "Café"}]
            self.assertValor(json.loads(caminho.read_text(encoding="utf-8")), esperado)
            self.assertValor(p.listar_eventos(caminho), esperado)
            self.assertValor(evento, {"tipo": " estudo ", "descricao": " Python "})

    def test_A22_03(self):
        r"""A22-03: Evento {}, tipo vazio, descrição numérica ou chave extra → ValueError: evento inválido; arquivo anterior intacto."""
        invalidos = [{}, {"tipo": " ", "descricao": "x"}, {"tipo": "x", "descricao": 3}, {"tipo": "x", "descricao": "y", "extra": 1}]
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "eventos.json"
            for evento in invalidos:
                caminho.write_bytes(b"[]")
                with self.assertRaises(ValueError) as erro:
                    p.registrar_evento(caminho, evento)
                self.assertEqual(str(erro.exception), "evento inválido")
                self.assertEqual(caminho.read_bytes(), b"[]")

    def test_A22_04(self):
        r"""A22-04: Evento inválido em caminho inexistente não cria arquivo."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "eventos.json"
            with self.assertRaises(ValueError):
                p.registrar_evento(caminho, {})
            self.assertFalse(caminho.exists())

    def test_A22_05(self):
        r"""A22-05: Histórico '{' causa JSONDecodeError; histórico '{}' causa ValueError: histórico deve ser lista; registrar preserva ambos."""
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "eventos.json"
            for texto, tipo in [("{", json.JSONDecodeError), ("{}", ValueError)]:
                caminho.write_text(texto, encoding="utf-8")
                with self.assertRaises(tipo) as erro:
                    p.listar_eventos(caminho)
                if texto == "{}":
                    self.assertEqual(str(erro.exception), "histórico deve ser lista")
                with self.assertRaises(tipo):
                    p.registrar_evento(caminho, {"tipo": "x", "descricao": "y"})
                self.assertEqual(caminho.read_text(encoding="utf-8"), texto)


if __name__ == "__main__":
    unittest.main()

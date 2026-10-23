"""Casos públicos da aula 29. Cada A29-NN está descrito em PRATICA.md."""

import unittest
import json
from urllib.parse import parse_qs, urlsplit
from testes.apoio import Contrato

from praticas.aula29_http_contratos import pratica as p


class TestAula29(Contrato):

    def test_A29_01(self):
        r"""A29-01: Parâmetros {q:'café & pão', pagina:'2'} voltam íntegros ao decodificar a URL; base preservada."""
        parametros = {"q": "café & pão", "pagina": "2"}
        url = p.montar_url("https://exemplo.invalid/busca", parametros)
        partes = urlsplit(url)
        self.assertEqual((partes.scheme, partes.netloc, partes.path), ("https", "exemplo.invalid", "/busca"))
        self.assertEqual(parse_qs(partes.query), {"q": ["café & pão"], "pagina": ["2"]})
        self.assertValor(parametros, {"q": "café & pão", "pagina": "2"})

    def test_A29_02(self):
        r"""A29-02: Parâmetros vazios → base exata, sem ?."""
        self.assertValor(p.montar_url("https://exemplo.invalid/itens", {}), "https://exemplo.invalid/itens")

    def test_A29_03(self):
        r"""A29-03: 200 com objeto, lista e null devolve dict, list e None correspondentes."""
        self.assertValor(p.interpretar_resposta(200, '{"ok": true}'), {"ok": True})
        self.assertValor(p.interpretar_resposta(200, "[1, 2]"), [1, 2])
        self.assertIsNone(p.interpretar_resposta(200, "null"))

    def test_A29_04(self):
        r"""A29-04: 200 com '{' → JSONDecodeError; 404 com texto não JSON → None."""
        with self.assertRaises(json.JSONDecodeError):
            p.interpretar_resposta(200, "{")
        self.assertIsNone(p.interpretar_resposta(404, "não é JSON"))

    def test_A29_05(self):
        r"""A29-05: Códigos 201, 400 e 500 → RuntimeError: HTTP 201, HTTP 400 e HTTP 500, respectivamente."""
        for status in [201, 400, 500]:
            with self.assertRaises(RuntimeError) as erro:
                p.interpretar_resposta(status, "não é JSON")
            self.assertEqual(str(erro.exception), f"HTTP {status}")


if __name__ == "__main__":
    unittest.main()

"""Comparações públicas: valores, tipos e tolerância declarada nos enunciados."""
import math
import unittest


class Contrato(unittest.TestCase):
    def assertValor(self, recebido, esperado, caminho="retorno"):
        self.assertIs(
            type(recebido), type(esperado),
            f"{caminho}: esperado tipo {type(esperado).__name__}, recebido {type(recebido).__name__}",
        )
        if isinstance(esperado, float):
            self.assertTrue(
                math.isclose(recebido, esperado, rel_tol=1e-9, abs_tol=1e-9),
                f"{caminho}: esperado {esperado!r}, recebido {recebido!r}",
            )
        elif isinstance(esperado, (list, tuple)):
            self.assertEqual(len(recebido), len(esperado), f"{caminho}: quantidade de elementos diferente")
            for indice, (real, previsto) in enumerate(zip(recebido, esperado)):
                self.assertValor(real, previsto, f"{caminho}[{indice}]")
        elif isinstance(esperado, dict):
            self.assertEqual(set(recebido), set(esperado), f"{caminho}: chaves diferentes")
            for chave in esperado:
                self.assertValor(recebido[chave], esperado[chave], f"{caminho}[{chave!r}]")
        else:
            self.assertEqual(recebido, esperado, f"{caminho}: valor diferente do contrato")

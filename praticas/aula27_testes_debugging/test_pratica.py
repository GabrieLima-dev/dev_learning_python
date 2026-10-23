import unittest
from praticas.aula27_testes_debugging import pratica


class TestFrete(unittest.TestCase):
    def test_abaixo_do_limite(self):
        # TODO: escolha uma entrada abaixo da gratuidade e confira seu frete.
        self.fail("Escreva seu teste para abaixo do limite")

    def test_no_limite(self):
        # TODO: confira exatamente a fronteira da gratuidade.
        self.fail("Escreva seu teste para o limite")

    def test_acima_do_limite(self):
        # TODO: confira um valor acima da fronteira.
        self.fail("Escreva seu teste para acima do limite")

    def test_negativo(self):
        # TODO: confira a exceção e a mensagem para total negativo.
        self.fail("Escreva seu teste para total negativo")

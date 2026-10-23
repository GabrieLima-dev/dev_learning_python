"""Prática 24: Dataclasses e composição de objetos. Leia PRATICA.md antes de editar."""

from dataclasses import dataclass


# TODO: transforme Item em dataclass congelada com os três campos exatos de PRATICA.md.
class Item:
    def subtotal(self):
        # TODO: devolva preço em centavos vezes quantidade como int.
        raise NotImplementedError("Implemente Item e subtotal")


class Carrinho:
    def __init__(self):
        # TODO: inicie a coleção de itens própria desta instância.
        raise NotImplementedError("Implemente Carrinho.__init__")

    def adicionar(self, item):
        # TODO: guarde mais uma ocorrência do item e retorne None.
        raise NotImplementedError("Implemente adicionar")

    def total(self):
        # TODO: some os subtotais dos itens; carrinho vazio tem total zero.
        raise NotImplementedError("Implemente total")

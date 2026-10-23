"""Prática 23: Classes, objetos e estado. Leia PRATICA.md antes de editar."""

class Conta:
    def __init__(self, titular, saldo=0):
        # TODO: guarde titular e saldo por instância; saldo negativo deve ser rejeitado.
        raise NotImplementedError("Implemente Conta.__init__")

    def depositar(self, valor):
        # TODO: valor deve ser positivo; em sucesso atualize e retorne saldo, sem mudar em erro.
        raise NotImplementedError("Implemente depositar")

    def sacar(self, valor):
        # TODO: rejeite valor não positivo e saldo insuficiente; sucesso devolve o saldo atualizado.
        raise NotImplementedError("Implemente sacar")

import sqlite3


class RepositorioTarefas:
    def __init__(self, caminho):
        # TODO: prepare o banco sem apagar dados; administre e feche as conexões que criar.
        raise NotImplementedError("Implemente RepositorioTarefas.__init__")

    def adicionar(self, titulo):
        # TODO: valide título normalizado de 1 a 80 caracteres, persista pendente e devolva id.
        raise NotImplementedError("Implemente adicionar")

    def listar(self, pendentes=False):
        # TODO: devolva dicts id/titulo/concluida por id, filtrando pendentes quando solicitado.
        raise NotImplementedError("Implemente listar")

    def concluir(self, identificador):
        # TODO: marque como concluída e persista; True se existe (mesmo concluída), False se ausente.
        raise NotImplementedError("Implemente concluir")

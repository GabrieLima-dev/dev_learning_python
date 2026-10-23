"""Prática 25: Herança e polimorfismo. Leia PRATICA.md antes de editar."""

class Forma:
    def area(self):
        # TODO: a forma genérica deve comunicar operação não implementada com NotImplementedError.
        raise NotImplementedError


class Retangulo(Forma):
    def __init__(self, largura, altura):
        # TODO: guarde as duas dimensões desta instância.
        raise NotImplementedError("Implemente Retangulo.__init__")

    def area(self):
        # TODO: devolva a área a partir das dimensões.
        raise NotImplementedError("Implemente Retangulo.area")


class Quadrado(Retangulo):
    def __init__(self, lado):
        # TODO: inicialize a especialização de Retangulo com lados iguais.
        raise NotImplementedError("Implemente Quadrado.__init__")


def total_areas(formas):
    # TODO: some area() dos objetos, sem exigir classe concreta; vazio deve resultar em zero.
    raise NotImplementedError("Implemente total_areas")

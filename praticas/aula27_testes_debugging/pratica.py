"""Prática 27: Escrita de testes e investigação de falhas. Leia PRATICA.md antes de editar."""

def frete(total_centavos):
    if total_centavos < 0:
        raise ValueError("total inválido")
    # TODO: investigue e corrija a fronteira da gratuidade conforme PRATICA.md.
    if total_centavos > 20000:
        return 0
    return 1200

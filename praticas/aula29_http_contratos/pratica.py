"""Prática 29: HTTP, URLs e contratos de resposta. Leia PRATICA.md antes de editar."""

import json
from urllib.parse import urlencode


def montar_url(base, parametros):
    # TODO: acrescente consulta codificada apenas se houver parâmetros, preservando o dict.
    raise NotImplementedError("Implemente montar_url")


def interpretar_resposta(status, corpo):
    # TODO: 200 interpreta JSON; 404 retorna None; demais códigos geram RuntimeError("HTTP N").
    raise NotImplementedError("Implemente interpretar_resposta")

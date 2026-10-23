"""Executa uma suíte em processo isolado e produz um comprovante de resultado.

O comprovante evita confundir encerramento prematuro do processo com testes verdes.
Não é um mecanismo de segurança contra adulteração deliberada do repositório.
"""
import json
from pathlib import Path
import sys
import unittest


def main(argv=None):
    argumentos = sys.argv[1:] if argv is None else argv
    modulo, destino = argumentos
    suite = unittest.defaultTestLoader.loadTestsFromName(modulo)
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    resumo = {
        "executados": resultado.testsRun,
        "falhas": len(resultado.failures),
        "erros": len(resultado.errors),
        "pulados": len(resultado.skipped),
        "falhas_esperadas": len(resultado.expectedFailures),
        "sucessos_inesperados": len(resultado.unexpectedSuccesses),
        "sucesso": resultado.wasSuccessful(),
    }
    Path(destino).write_text(json.dumps(resumo), encoding="utf-8")
    return 0 if resumo["sucesso"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

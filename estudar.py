"""Entrada da trilha. Execute este arquivo a partir da raiz do projeto."""
import sys

if sys.version_info < (3, 11):
    print("Esta trilha requer Python 3.11 ou superior. Consulte o README.md.", file=sys.stderr)
    raise SystemExit(2)

from sistema.cli import main

if __name__ == "__main__":
    raise SystemExit(main())

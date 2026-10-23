"""Manutenção do professor: atualiza assinaturas após uma revisão do núcleo.

Não use este comando como aluno para aceitar mudanças nos testes de avaliação.
"""
import hashlib
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def main():
    arquivos = [RAIZ / "estudar.py", RAIZ / "curriculum/python.json"]
    for pasta in ["sistema", "testes"]:
        arquivos.extend((RAIZ / pasta).rglob("*.py"))
    manifesto = {
        "versao": 1,
        "arquivos": {
            caminho.relative_to(RAIZ).as_posix(): hashlib.sha256(caminho.read_bytes()).hexdigest()
            for caminho in sorted(arquivos)
        },
    }
    destino = RAIZ / "curriculum/integridade.json"
    destino.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Manifesto atualizado para {len(arquivos)} arquivos. Revise o diff e execute estudar.py verificar.")


if __name__ == "__main__":
    main()

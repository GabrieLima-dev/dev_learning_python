"""Valida documentos, vínculos e contagem de casos sem importar código do aluno."""
import ast
from pathlib import Path
import re
from urllib.parse import unquote


def verificar_estrutura(raiz, aulas):
    erros = []
    for aula in aulas:
        teste = raiz / aula["teste"]
        try:
            arvore = ast.parse(teste.read_text(encoding="utf-8"))
            metodos = [no.name for no in ast.walk(arvore) if isinstance(no, ast.FunctionDef) and no.name.startswith("test_")]
            if len(metodos) != aula["casos"]:
                erros.append(f"{teste}: contagem de casos difere do currículo")
            enunciado = (raiz / aula["pratica"]).read_text(encoding="utf-8")
            for i in range(1, aula["casos"] + 1):
                if f"A{aula['id']}-{i:02d}" not in enunciado:
                    erros.append(f"Caso A{aula['id']}-{i:02d} ausente do enunciado")
        except SyntaxError as erro:
            erros.append(f"Teste com sintaxe inválida: {teste}: {erro}")
    documentos = [raiz / "README.md", *list((raiz / "estudos").rglob("*.md")), *list((raiz / "praticas").rglob("*.md")), *list((raiz / "docs").glob("*.md"))]
    for documento in documentos:
        if not documento.exists():
            erros.append(f"Documento ausente: {documento}")
            continue
        texto = documento.read_text(encoding="utf-8")
        # A sintaxe dos exemplos também deve ser válida quando copiada pelo aluno.
        for exemplo in re.findall(r"```python\n(.*?)```", texto, flags=re.DOTALL):
            try:
                ast.parse(exemplo)
            except SyntaxError as erro:
                erros.append(f"Exemplo Python inválido em {documento.relative_to(raiz)}: {erro}")
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", texto):
            if "://" in link or link.startswith("#") or link.startswith("mailto:"):
                continue
            relativo = unquote(link.split("#", 1)[0])
            if not (documento.parent / relativo).exists():
                erros.append(f"Link local quebrado em {documento.relative_to(raiz)}: {link}")
    return erros

# 16 — Módulos, pacotes e anotações de tipo

**Objetivo:** Distribuir uma regra e sua composição entre dois módulos.

Um módulo é um arquivo Python que pode ser importado. Um pacote organiza módulos em uma pasta. Este projeto usa arquivos `__init__.py` para tornar essa organização explícita. Um caminho como `praticas.aula16_modulos.operacoes` localiza um módulo dentro dos pacotes.

Importar executa as instruções da raiz do arquivo. Por isso, definições de funções e constantes são adequadas ali, mas uma pergunta com input ou uma escrita em arquivo pode surpreender quem apenas queria reutilizar uma função. Para programas executáveis, o bloco `if __name__ == "__main__":` permite separar o ponto de entrada da importação.

Uma anotação como `def dobro(valor: int) -> int` documenta os tipos esperados. Python não converte nem valida automaticamente os valores por causa dela. A anotação ajuda leitores, editores e ferramentas específicas. O comportamento continua sendo responsabilidade do código e dos testes.

A organização deve acompanhar responsabilidades. Nesta aula, o módulo operacoes contém uma regra pequena e pratica coordena uma lista de itens usando essa regra. O import torna a colaboração explícita e evita copiar a mesma conta para vários lugares.

Para que os imports funcionem sem configurações especiais, execute comandos a partir da raiz do repositório. Evite renomear pacotes e funções fornecidos. Você pode testar o arquivo de prática pelo comando da trilha sem precisar executar cada arquivo Python diretamente.

## Exemplo comentado

```python
# Exemplo de assinatura com anotação:
def comprimento(texto: str) -> int:
    return len(texto)

# A anotação informa a intenção; não substitui uma validação.
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Minha importação não executa interação ou escrita em arquivo.
- [ ] Consigo explicar por que a anotação não valida o valor em tempo de execução.

Abra o [enunciado](../../../praticas/aula16_modulos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula16_modulos/pratica.py) e consulte o [teste público](../../../testes/test_aula16_modulos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 16
```

```powershell
# Windows
py -3 estudar.py testar 16
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

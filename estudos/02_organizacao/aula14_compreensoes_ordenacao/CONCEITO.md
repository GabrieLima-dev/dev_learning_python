# 14 — Compreensões e ordenação

**Objetivo:** Filtrar e transformar valores, depois ordenar registros por dois critérios.

Uma compreensão de lista expressa uma transformação de forma compacta. Em `[expressao for item in origem if condicao]`, a origem fornece os valores, a condição escolhe quais entram e a expressão define o que será colocado no resultado. O filtro é opcional.

Use compreensões quando a transformação é curta e compreensível. Elas não substituem todos os laços. Se você precisa de muitos efeitos colaterais ou vários ramos, um for explícito costuma ser mais fácil de ler. Nesta prática, a primeira função é pequena e serve para experimentar a sintaxe.

`sorted` devolve uma nova lista. Já `lista.sort()` altera a própria lista e devolve None. O argumento `key` informa como comparar cada elemento. Uma função lambda é uma função curta escrita como expressão; `lambda item: item["nome"]` extrai o nome para ordenação.

Uma tupla pode representar vários critérios de ordenação. Python compara o primeiro elemento; se empatar, compara o seguinte. Para notas em ordem decrescente e nomes em ordem crescente, cada critério precisa expressar sua própria direção. Usar reverse em toda a lista também inverteria os nomes.

Ordenação é estável: itens com a mesma chave mantêm a ordem relativa original. O contrato desta aula permite compartilhar os dicionários internos porque não pede cópia profunda; exige uma lista nova e proíbe modificações nos registros. Documentar isso evita confundir identidade dos objetos com igualdade dos dados.

## Exemplo comentado

```python
palavras = ["sol", "montanha", "lua"]
tamanhos = [len(palavra) for palavra in palavras if len(palavra) > 3]
print(tamanhos)  # [8]
print(sorted(palavras, key=lambda palavra: len(palavra)))
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Minha compreensão continua legível.
- [ ] Consigo explicar o desempate e a diferença entre sorted e sort.

Abra o [enunciado](../../../praticas/aula14_compreensoes_ordenacao/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula14_compreensoes_ordenacao/pratica.py) e consulte o [teste público](../../../testes/test_aula14_compreensoes_ordenacao.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 14
```

```powershell
# Windows
py -3 estudar.py testar 14
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

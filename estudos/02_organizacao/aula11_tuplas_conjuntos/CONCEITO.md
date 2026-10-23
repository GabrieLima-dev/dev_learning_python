# 11 — Tuplas, conjuntos e desempacotamento

**Objetivo:** Escolher estruturas conforme ordem, posição e duplicação.

Uma tupla agrupa valores em ordem e não permite trocar seus elementos. É útil para representar um par, como latitude e longitude. Tuplas normalmente usam parênteses: `(3, 4)`. Uma tupla de um elemento precisa de vírgula: `(3,)`. A vírgula é importante para que Python não interprete apenas uma expressão entre parênteses.

Desempacotamento atribui os elementos a vários nomes: `x, y = ponto`. A quantidade de nomes precisa corresponder à quantidade de elementos. `split(separador)` divide uma string em uma lista de partes; cada parte ainda é texto e pode precisar de conversão.

Um conjunto, ou set, representa valores únicos. Ele não deve ser usado para prometer uma ordem de exibição. `set(lista)` elimina duplicados. A interseção, obtida por `a & b`, contém apenas os elementos presentes nos dois conjuntos. A união usa `|`, e a diferença usa `-`.

Quando o resultado precisa ter ordem, transforme os valores com `sorted`, que devolve uma nova lista ordenada. Essa separação é útil: o conjunto decide quais valores existem; a lista ordenada decide como apresentá-los.

A prática contrasta os dois tipos. Coordenadas têm duas posições com significado, mesmo que os números sejam iguais. Itens em comum não precisam repetir ocorrências, mas devem ser devolvidos numa ordem estável. Use o tipo pedido: uma lista com dois números não é uma tupla.

## Exemplo comentado

```python
ponto = (2.0, 5.0)
x, y = ponto
print(x, y)
cores = {"azul", "verde"} & {"verde", "roxo"}
print(sorted(cores))  # ['verde']
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Sei explicar por que o conjunto não é a saída final ordenada.
- [ ] Usei uma tupla para o par de coordenadas.

Abra o [enunciado](../../../praticas/aula11_tuplas_conjuntos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula11_tuplas_conjuntos/pratica.py) e consulte o [teste público](../../../testes/test_aula11_tuplas_conjuntos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 11
```

```powershell
# Windows
py -3 estudar.py testar 11
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

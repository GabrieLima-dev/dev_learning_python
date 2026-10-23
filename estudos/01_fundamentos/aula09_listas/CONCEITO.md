# 09 — Listas e preservação dos dados

**Objetivo:** Filtrar e reorganizar listas sem alterar os argumentos.

Uma lista armazena vários valores em ordem. Ela usa colchetes: `[10, 20, 30]`. O primeiro índice é zero. `lista[0]` acessa o primeiro elemento e `lista[-1]` acessa o último. Uma lista vazia não possui esses elementos: tentar acessá-los provoca IndexError.

Listas são mutáveis. `append` acrescenta um elemento, `pop` remove e devolve um elemento, e atribuir em um índice substitui um valor. Dois nomes podem apontar para a mesma lista. Escrever `copia = original` não cria uma lista independente; mudanças por um nome aparecerão pelo outro.

Um fatiamento como `lista[1:]` produz uma nova lista com parte dos elementos. `lista[:]` copia a lista superficialmente. Nesta aula todos os elementos são inteiros, então essa cópia é suficiente. Para estruturas com listas internas, uma cópia superficial ainda compartilha os elementos internos; estudaremos esse cuidado em exercícios com registros.

Você pode percorrer uma lista com for sem precisar de índices. Para filtrar valores, construa o resultado separadamente. Remover itens da lista enquanto a percorre pode fazer elementos serem pulados. Além disso, a prática exige preservar os dados recebidos.

O contrato determina se a função pode alterar a entrada. Aqui a resposta é não. Os testes guardam uma cópia dos valores originais e conferem tanto o resultado quanto a preservação da lista. Uma lista vazia é um caso normal, não um erro.

## Exemplo comentado

```python
cores = ["azul", "verde"]
copia = cores[:]
copia.append("roxo")
print(cores)  # ['azul', 'verde']
print(copia)  # ['azul', 'verde', 'roxo']
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Sei distinguir copiar uma lista de atribuí-la a outro nome.
- [ ] Minhas funções preservam a entrada e funcionam com lista vazia.

Abra o [enunciado](../../../praticas/aula09_listas/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula09_listas/pratica.py) e consulte o [teste público](../../../testes/test_aula09_listas.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 09
```

```powershell
# Windows
py -3 estudar.py testar 09
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

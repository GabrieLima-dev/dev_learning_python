# 12 — Dicionários e agregação

**Objetivo:** Contar ocorrências e calcular valores a partir de registros.

Um dicionário associa chaves a valores. Em `{"caderno": 3}`, a chave é o texto caderno e o valor é o inteiro 3. Acesso por chave usa colchetes. Uma chave inexistente provoca KeyError; `get(chave, padrao)` permite definir o valor para a ausência.

Dicionários são mutáveis. Atribuir `dados[chave] = valor` cria ou atualiza a associação. Percorrer um dicionário diretamente percorre suas chaves. `items()` permite obter pares de chave e valor; `values()` percorre somente os valores.

Uma agregação reúne vários registros em uma informação menor. Para contar votos, cada candidato é uma chave e o valor é a quantidade acumulada. A primeira ocorrência exige considerar que a chave ainda não existe. Cada ocorrência seguinte aumenta a contagem, sem duplicar a chave.

Também é possível reunir vários dados sobre um item em um dicionário. Por exemplo, o cadastro de um produto pode conter preço e quantidade. Uma lista desses cadastros representa vários produtos. Leia o contrato para descobrir os nomes exatos das chaves: `preco_centavos` e `preco` seriam campos diferentes.

Não acrescente normalizações que não foram pedidas. Nesta prática, `Ana` e `ana` são candidatos diferentes. Funções de agregação devem construir o resultado sem alterar os registros recebidos, pois eles podem ser usados em outra parte do programa depois.

## Exemplo comentado

```python
compras = {"livro": 2}
compras["caneta"] = compras.get("caneta", 0) + 1
for nome, quantidade in compras.items():
    print(nome, quantidade)
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo explicar o valor padrão para uma chave nova.
- [ ] Não alterei os registros recebidos.

Abra o [enunciado](../../../praticas/aula12_dicionarios/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula12_dicionarios/pratica.py) e consulte o [teste público](../../../testes/test_aula12_dicionarios.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 12
```

```powershell
# Windows
py -3 estudar.py testar 12
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

# 13 — Funções, parâmetros e composição

**Objetivo:** Definir um valor padrão e reutilizar uma regra em uma função maior.

Até aqui você completou funções já declaradas. Agora vamos observar como a divisão em funções reduz repetição e dá nome às regras. Uma função recebe argumentos, realiza uma tarefa e pode devolver um resultado. Uma variável criada dentro dela é local àquela chamada.

Parâmetros podem ter valores padrão, como `def mensagem(nome, prefixo="Oi")`. Quem chama pode omitir prefixo ou fornecer outro valor. Também pode usar argumentos por nome: `mensagem("Rui", prefixo="Olá")`. O nome do parâmetro passa a fazer parte da interface pública; não o altere quando testes e outros módulos dependem dele.

Evite usar uma lista mutável como valor padrão quando pretende criar uma nova lista a cada chamada. O objeto padrão é criado uma vez ao definir a função, e seu conteúdo pode vazar entre chamadas. Valores imutáveis, como números e strings, não possuem esse problema de mutação.

Composição significa usar o resultado de uma função em outra tarefa. Se um pedido utiliza a mesma regra de desconto de um item, chame a função que já representa essa regra. Assim a regra fica definida em um lugar. Os testes desta aula verificam os resultados; cabe ao seu checklist conferir se a regra foi realmente reaproveitada.

Um contrato também deve definir arredondamento. Aqui trabalharemos em centavos e descartaremos a fração final de centavo depois de aplicar o percentual. Aplicar o desconto a cada item e somar depois pode produzir diferença de centavos em relação a descontar do total. Leia a regra antes de escolher.

## Exemplo comentado

```python
def adicionar_taxa(valor, taxa=2):
    return valor + taxa

print(adicionar_taxa(10))  # 12
print(adicionar_taxa(10, taxa=5))  # 15
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Reaproveitei aplicar_desconto dentro de total_com_desconto.
- [ ] Sei explicar por que o desconto é aplicado após a soma.

Abra o [enunciado](../../../praticas/aula13_funcoes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula13_funcoes/pratica.py) e consulte o [teste público](../../../testes/test_aula13_funcoes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 13
```

```powershell
# Windows
py -3 estudar.py testar 13
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

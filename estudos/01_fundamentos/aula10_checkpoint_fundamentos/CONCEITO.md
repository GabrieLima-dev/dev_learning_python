# 10 — Checkpoint: relatório de notas

**Objetivo:** Integrar os fundamentos em um relatório com média e contagem.

Um checkpoint reúne assuntos já estudados em uma tarefa maior. Você já sabe receber parâmetros, calcular, decidir, repetir, lidar com listas e formatar strings. Agora essas partes precisam trabalhar juntas para produzir um pequeno relatório.

Antes de escrever, identifique entrada, processamento e saída. A entrada é uma lista de notas. O processamento reúne quantidade, média e número de aprovados. A saída é uma única string com formato fixo. Nenhum input é necessário porque a lista já chega por parâmetro.

A média aritmética é a soma dividida pela quantidade. A lista vazia precisa de uma regra própria para não dividir por zero. O enunciado estabelece média zero nesse caso. Contar aprovados é uma tarefa diferente de calcular a média: a nota mínima para aprovação é 7 e precisa ser incluída.

Uma f-string pode formatar casas decimais com `:.2f`. Isso produz texto com duas casas, inclusive zeros finais. Não troca o separador decimal por vírgula. A formatação deve acontecer ao apresentar o resultado; usar textos no meio dos cálculos dificulta a solução.

Não tente reconhecer as listas dos testes pelo conteúdo. Faça o relatório funcionar para qualquer lista no domínio permitido. Depois de passar, explique verbalmente o que ocorreria com uma nova lista inventada por você. Essa explicação complementa os testes, que têm quantidade finita de casos.

Este checkpoint precisa ser concluído antes de registrar avanço no próximo módulo. Os materiais seguintes continuam disponíveis para leitura. Revise também status e diff e faça um commit coerente; se usa uma cópia no GitHub, sincronize após conferir o remoto.

## Exemplo comentado

```python
media = 8 / 3
print(f"Resultado: {media:.2f}")  # Resultado: 2.67
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo explicar cada parte do relatório sem ler uma solução.
- [ ] Tratei a lista vazia antes de dividir.
- [ ] Revisei meu diff, fiz um commit e sincronizei minha cópia no GitHub, se configurada.

Abra o [enunciado](../../../praticas/aula10_checkpoint_fundamentos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula10_checkpoint_fundamentos/pratica.py) e consulte o [teste público](../../../testes/test_aula10_checkpoint_fundamentos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 10
```

```powershell
# Windows
py -3 estudar.py testar 10
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

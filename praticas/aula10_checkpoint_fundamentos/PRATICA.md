# Prática 10 — Checkpoint: relatório de notas

**Objetivo:** Integrar os fundamentos em um relatório com média e contagem.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula10_checkpoint_fundamentos/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`relatorio_notas(notas)`: recebe lista de int ou float entre 0 e 10, sem valores inválidos. Devolve exatamente `Quantidade: N | Média: M | Aprovados: A`, em que N é o tamanho, M é a média com duas casas decimais e ponto, e A é a quantidade de notas maiores ou iguais a 7. Lista vazia: N=0, M=0.00 e A=0. Não modifique notas e não imprima. Use a formatação padrão do Python `:.2f` para o arredondamento.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A10-01 | [] → "Quantidade: 0 &#124; Média: 0.00 &#124; Aprovados: 0". |
| A10-02 | [7] → "Quantidade: 1 &#124; Média: 7.00 &#124; Aprovados: 1". |
| A10-03 | [10, 5, 7] → "Quantidade: 3 &#124; Média: 7.33 &#124; Aprovados: 2". |
| A10-04 | [6.9, 7.1, 0] → "Quantidade: 3 &#124; Média: 4.67 &#124; Aprovados: 1"; preserva entrada. |
| A10-05 | [0, 0] → "Quantidade: 2 &#124; Média: 0.00 &#124; Aprovados: 0". |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 10
```

```powershell
# Windows
py -3 estudar.py testar 10
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula10_checkpoint_fundamentos -v` (Windows: `py -3 -m unittest testes.test_aula10_checkpoint_fundamentos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A10-NN nesta tabela e [o código do teste](../../testes/test_aula10_checkpoint_fundamentos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo explicar cada parte do relatório sem ler uma solução.
- [ ] Tratei a lista vazia antes de dividir.
- [ ] Revisei meu diff, fiz um commit e sincronizei minha cópia no GitHub, se configurada.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

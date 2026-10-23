# Prática 14 — Compreensões e ordenação

**Objetivo:** Filtrar e transformar valores, depois ordenar registros por dois critérios.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula14_compreensoes_ordenacao/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`quadrados_pares(numeros)`: recebe lista de inteiros; devolve nova lista com o quadrado de cada número par, mantendo ordem e repetições. Zero e negativos pares entram.

`ordenar_alunos(alunos)`: recebe lista de dicts com nome string e nota numérica. Retorna nova lista ordenada por nota decrescente; em empate, nome crescente pela comparação padrão de strings do Python, sensível a caixa e acentos. Não altera lista nem dicts de entrada. Não é exigida cópia dos dicts internos. Pratique uma compreensão na primeira função e uma chave de ordenação na segunda.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A14-01 | quadrados_pares([-2, 3, 0, 4, 4]) → [4, 0, 16, 16]. |
| A14-02 | quadrados_pares([]) e quadrados_pares([1, 3]) → []. |
| A14-03 | Bia 8, Ana 8, Rui 10 → Rui 10, Ana 8, Bia 8; entrada preservada. |
| A14-04 | ordenar_alunos([]) → uma nova lista vazia. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 14
```

```powershell
# Windows
py -3 estudar.py testar 14
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula14_compreensoes_ordenacao -v` (Windows: `py -3 -m unittest testes.test_aula14_compreensoes_ordenacao -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A14-NN nesta tabela e [o código do teste](../../testes/test_aula14_compreensoes_ordenacao.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Minha compreensão continua legível.
- [ ] Consigo explicar o desempate e a diferença entre sorted e sort.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

# Prática 30 — Concorrência com tarefas independentes

**Objetivo:** Executar tarefas independentes simultaneamente, preservando ordem e propagando falhas.

Leia primeiro o [conceito](../../estudos/05_aplicacoes/aula30_concorrencia/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`executar_em_ordem(funcao, itens)`: itens é uma lista; funcao aceita um item e é segura para threads. Execute com pelo menos dois trabalhadores disponíveis, retorne lista dos resultados na ordem de itens, mesmo que a execução seja concorrente. Lista vazia retorna []. Preserve itens. Cada item deve ser processado uma vez.

Se funcao levantar exceção, propague essa exceção (tipo e mensagem), sem substituir por None ou texto. Encerre os trabalhadores ao sair. Use ThreadPoolExecutor. O teste da barreira exige que duas chamadas possam estar ativas ao mesmo tempo; ele permite até cinco segundos de espera para acomodar a máquina.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A30-01 | Aplicar quadrado a [3, 1, 2] → [9, 1, 4], preservando entrada; vazio → []. |
| A30-02 | Duas tarefas passam juntas por Barrier(2), uma chamada por item, e retornam [20, 10] na ordem de [2, 1]. |
| A30-03 | Tarefa que levanta ValueError("falha de tarefa") faz a função propagar tipo e mensagem. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 30
```

```powershell
# Windows
py -3 estudar.py testar 30
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula30_concorrencia -v` (Windows: `py -3 -m unittest testes.test_aula30_concorrencia -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A30-NN nesta tabela e [o código do teste](../../testes/test_aula30_concorrencia.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo explicar por que as tarefas da prática podem ser independentes.
- [ ] A ordem do resultado acompanha a entrada e falhas não são ocultadas.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

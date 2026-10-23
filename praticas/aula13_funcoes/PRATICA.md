# Prática 13 — Funções, parâmetros e composição

**Objetivo:** Definir um valor padrão e reutilizar uma regra em uma função maior.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula13_funcoes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`aplicar_desconto(valor_centavos, percentual=10)`: recebe inteiros, valor não negativo e percentual entre 0 e 100. Retorna int com o valor restante após o desconto, descartando fração de centavo ao final. Exemplo: 101 com 10% resulta em 90, pois 90.9 é reduzido a 90.

`total_com_desconto(precos, percentual=10)`: recebe lista de inteiros não negativos e o mesmo percentual. Soma os preços e aplica a regra ao total uma única vez; retorna int e preserva a lista. Use `aplicar_desconto` dentro dessa função como prática de composição. Lista vazia retorna 0. As duas aceitam percentual por nome.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A13-01 | aplicar_desconto(1000) → 900; (101) → 90. |
| A13-02 | aplicar_desconto(250, percentual=0) → 250; percentual=100 → 0. |
| A13-03 | aplicar_desconto(999, 25) → 749; valor zero → 0. |
| A13-04 | total_com_desconto([101, 101]) → 181, com entrada preservada. |
| A13-05 | total_com_desconto([], percentual=30) → 0; [200, 300] com 20% → 400. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 13
```

```powershell
# Windows
py -3 estudar.py testar 13
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula13_funcoes -v` (Windows: `py -3 -m unittest testes.test_aula13_funcoes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A13-NN nesta tabela e [o código do teste](../../testes/test_aula13_funcoes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Reaproveitei aplicar_desconto dentro de total_com_desconto.
- [ ] Sei explicar por que o desconto é aplicado após a soma.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

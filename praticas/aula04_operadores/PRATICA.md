# Prática 04 — Operadores e contas com inteiros

**Objetivo:** Calcular um pedido e decompor minutos sem misturar tipos ou unidades.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula04_operadores/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`total_pedido(preco_centavos, quantidade, desconto_centavos)`: recebe inteiros não negativos; o desconto não excede o subtotal. Retorna um inteiro: preço vezes quantidade menos o desconto total. Não há frete.

`horas_completas(minutos)` e `minutos_restantes(minutos)`: recebem um inteiro não negativo. Retornam inteiros correspondentes a grupos de 60 e ao restante de 0 a 59. Nenhuma função imprime.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A04-01 | Pedido (1250, 3, 250) → 3500 centavos. |
| A04-02 | Pedido (0, 2, 0) e (100, 0, 0) → 0. |
| A04-03 | Pedido (900, 1, 900) → 0; (101, 2, 1) → 201. |
| A04-04 | 0 minutos → 0 horas e 0 restantes. |
| A04-05 | 59 minutos → 0 horas e 59 restantes. |
| A04-06 | 60 minutos → 1 hora e 0 restantes; 135 → 2 e 15. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 04
```

```powershell
# Windows
py -3 estudar.py testar 04
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula04_operadores -v` (Windows: `py -3 -m unittest testes.test_aula04_operadores -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A04-NN nesta tabela e [o código do teste](../../testes/test_aula04_operadores.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Sei explicar por que / e // têm resultados diferentes.
- [ ] O desconto foi aplicado uma vez ao pedido e todas as quantias usam centavos.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

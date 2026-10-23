# Prática 21 — Datas e números decimais

**Objetivo:** Calcular intervalos reais de datas e somar valores com arredondamento definido.

Leia primeiro o [conceito](../../estudos/03_persistencia/aula21_datas_decimal/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`dias_entre(inicio, fim)`: recebe datas válidas como strings AAAA-MM-DD; retorna int igual a fim menos inicio em dias. Datas iguais resultam em 0 e ordem invertida resulta em número negativo.

`somar_precos(textos)`: recebe lista de strings decimais finitas, positivas, negativas ou zero, de até 6 dígitos inteiros e 4 casas. Retorna Decimal com duas casas, somando antes de arredondar uma única vez com ROUND_HALF_UP. Lista vazia retorna Decimal("0.00"). Preserve a entrada. Não use float como etapa intermediária.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A21-01 | 2024-02-28 até 2024-03-01 → 2 dias; 2023 no mesmo intervalo → 1. |
| A21-02 | 2025-01-01 até a mesma data → 0; 2025-01-03 até 2025-01-01 → -2. |
| A21-03 | ["0.10", "0.20"] → Decimal("0.30") com duas casas; preserva lista. |
| A21-04 | ["0.005", "0.005"] → Decimal("0.01"), arredondando apenas a soma. |
| A21-05 | ["-1.005"] → Decimal("-1.01"); [] → Decimal("0.00") com duas casas. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 21
```

```powershell
# Windows
py -3 estudar.py testar 21
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula21_datas_decimal -v` (Windows: `py -3 -m unittest testes.test_aula21_datas_decimal -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A21-NN nesta tabela e [o código do teste](../../testes/test_aula21_datas_decimal.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Não converti dinheiro em float antes de criar Decimal.
- [ ] Consigo explicar a ordem da subtração de datas e o momento do arredondamento.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

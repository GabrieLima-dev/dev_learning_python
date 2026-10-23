# 04 — Operadores e contas com inteiros

**Objetivo:** Calcular um pedido e decompor minutos sem misturar tipos ou unidades.

Expressões combinam valores e operadores. A multiplicação e a divisão acontecem antes da soma e da subtração. Parênteses deixam a intenção explícita e podem mudar a ordem. Por exemplo, `(2 + 3) * 4` resulta em 20; `2 + 3 * 4` resulta em 14.

Em Python, `/` sempre realiza divisão comum e costuma devolver um float. `//` realiza divisão pelo piso, e `%` devolve o resto correspondente. Para valores não negativos, isso permite separar uma quantidade em grupos completos e unidades que sobraram. `**` calcula potência.

Valores em dinheiro nesta parte da trilha serão inteiros em centavos: 1090 representa R$ 10,90. Assim, somar e multiplicar quantias inteiras não introduz aproximações decimais. Não misture reais e centavos dentro de uma mesma conta. Uma variável chamada `preco_centavos` comunica sua unidade.

A prática pede funções pequenas. Os parâmetros já trazem números corretos e não negativos; não é necessário pedir dados, arredondar floats nem acrescentar validações. O desconto é um valor total em centavos, aplicado uma única vez ao pedido. Desconto por unidade seria outra regra e produziria um resultado diferente.

Ao verificar uma conta, escreva primeiro as unidades: preço em centavos vezes quantidade resulta em centavos; em seguida subtraia o desconto também em centavos. Casos com zero ajudam a descobrir suposições incorretas, como retornar sempre um preço mínimo.

## Exemplo comentado

```python
segundos = 135
minutos = segundos // 60
restante = segundos % 60
print(minutos, restante)  # 2 15
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Sei explicar por que / e // têm resultados diferentes.
- [ ] O desconto foi aplicado uma vez ao pedido e todas as quantias usam centavos.

Abra o [enunciado](../../../praticas/aula04_operadores/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula04_operadores/pratica.py) e consulte o [teste público](../../../testes/test_aula04_operadores.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 04
```

```powershell
# Windows
py -3 estudar.py testar 04
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

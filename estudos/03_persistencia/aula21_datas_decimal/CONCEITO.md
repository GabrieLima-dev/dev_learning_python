# 21 — Datas e números decimais

**Objetivo:** Calcular intervalos reais de datas e somar valores com arredondamento definido.

Uma data de calendário não é apenas uma string. A classe date do módulo datetime representa ano, mês e dia e valida combinações possíveis. `date.fromisoformat` interpreta o formato AAAA-MM-DD. Subtrair duas datas produz um timedelta, cuja propriedade days informa a diferença em dias.

Essa diferença considera meses com tamanhos distintos e anos bissextos. Não estime um mês como trinta dias se precisa da diferença real entre datas. A ordem da subtração importa: final menos inicial é positiva quando a data final vem depois.

Números float usam representação binária e muitas frações decimais não são exatas nela. Decimal, do módulo decimal, representa números em base decimal. Construa Decimal a partir do texto original para evitar carregar uma aproximação que já existia em um float.

Dinheiro exige uma política de arredondamento. `quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` fixa duas casas e resolve os empates afastando do zero. Arredondar cada parcela e depois somar pode ser diferente de somar primeiro e arredondar uma única vez.

Nesta atividade as datas são válidas e os valores monetários são textos decimais finitos pequenos. Não é necessário tratar fuso horário, infinitos ou NaN. Separar esse domínio deixa claro o que está sendo aprendido e evita inventar regras que o teste não cobra.

## Exemplo comentado

```python
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

intervalo = date(2025, 1, 4) - date(2025, 1, 1)
print(intervalo.days)  # 3
valor = Decimal("2.345")
print(valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  # 2.35
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Não converti dinheiro em float antes de criar Decimal.
- [ ] Consigo explicar a ordem da subtração de datas e o momento do arredondamento.

Abra o [enunciado](../../../praticas/aula21_datas_decimal/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula21_datas_decimal/pratica.py) e consulte o [teste público](../../../testes/test_aula21_datas_decimal.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 21
```

```powershell
# Windows
py -3 estudar.py testar 21
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

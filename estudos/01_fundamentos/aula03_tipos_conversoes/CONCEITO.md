# 03 — Variáveis, tipos e conversões

**Objetivo:** Converter entradas textuais e distinguir números, textos e booleanos.

Uma variável associa um nome a um valor: `idade = 19`. O tipo pertence ao valor. `int` representa inteiros, `float` representa números com parte decimal, `str` representa texto e `bool` representa verdadeiro ou falso. `True` e `False` começam com maiúscula e não usam aspas.

O texto `"12"` e o número `12` não são iguais. Somar duas strings concatena textos; somar dois inteiros faz uma conta. Para transformar um texto numérico em inteiro, use `int(texto)`. Para obter número decimal, use `float(texto)`, com ponto decimal no texto. `str(valor)` faz o caminho para texto. A conversão pode falhar se o conteúdo não representar um número; estudaremos tratamento dessas falhas adiante.

Funções recebem dados por parâmetros. Na estrutura `def exemplo(texto):`, o nome `texto` passa a representar o argumento fornecido em cada chamada. O teste pode chamar a mesma função com valores diferentes. Evite escrever uma resposta fixa para um exemplo: calcule a partir do parâmetro.

Operadores produzem novos valores: `*` multiplica números, `+` soma, e `==` compara dois valores e devolve um booleano. Atribuição usa um único `=`. Uma comparação não altera o valor comparado. `type(valor)` ajuda a observar o tipo durante um experimento no terminal interativo.

Nesta prática, os textos numéricos são válidos. Seu foco é converter antes de calcular e devolver o tipo solicitado. Não acrescente input às funções: os testes já entregam os dados pelos parâmetros.

## Exemplo comentado

```python
quantidade_texto = "8"
quantidade = int(quantidade_texto)
print(quantidade + 2)  # 10
print(quantidade == 8)  # True
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo explicar a diferença entre "12" e 12.
- [ ] Minhas funções devolvem int e bool, conforme o contrato.

Abra o [enunciado](../../../praticas/aula03_tipos_conversoes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula03_tipos_conversoes/pratica.py) e consulte o [teste público](../../../testes/test_aula03_tipos_conversoes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 03
```

```powershell
# Windows
py -3 estudar.py testar 03
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

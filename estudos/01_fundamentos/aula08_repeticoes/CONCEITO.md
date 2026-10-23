# 08 — Repetições, contadores e acumuladores

**Objetivo:** Construir acumulações e contagens com limites corretos.

Um laço repete uma ação. `for` percorre os valores de uma sequência ou de um range. `range(inicio, fim)` inclui o início e exclui o fim. `range(4)` produz 0, 1, 2 e 3. Se a regra inclui a fronteira final, pense na diferença entre a regra e esse limite exclusivo.

Um acumulador guarda um resultado parcial, como a soma do que já foi processado. Ele precisa de um valor inicial coerente: para uma soma, zero funciona mesmo quando nenhum elemento é visitado. Um contador registra quantas vezes uma condição ocorreu; ele aumenta somente nos casos relevantes.

`while` repete enquanto uma condição for verdadeira. O corpo deve fazer o programa caminhar até uma condição de parada. Se o estado nunca muda, pode surgir um laço infinito. O comando de testes deste projeto tem um limite de duração para impedir que uma tentativa travada deixe o aluno sem resposta.

`break` encerra um laço e `continue` passa à próxima repetição. Não são necessários em todo exercício. Prefira uma condição simples quando ela já descreve o problema. O operador `%` permite descobrir se um inteiro é divisível por outro: resto zero indica divisão exata.

Nesta aula, pratique pelo menos um laço na solução, mesmo que conheça uma fórmula matemática. Os testes verificam o resultado; a autoavaliação lembra o conceito que deve ser exercitado. Entrada zero e intervalo invertido mostram o que acontece quando não existe nenhum elemento para acumular.

## Exemplo comentado

```python
produto = 1
for numero in range(1, 5):
    produto = produto * numero
print(produto)  # 24
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Usei laços e sei explicar o valor inicial do acumulador.
- [ ] Sei por que o fim de range não faz parte da repetição.

Abra o [enunciado](../../../praticas/aula08_repeticoes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula08_repeticoes/pratica.py) e consulte o [teste público](../../../testes/test_aula08_repeticoes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 08
```

```powershell
# Windows
py -3 estudar.py testar 08
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

# 07 — Decisões e expressões booleanas

**Objetivo:** Classificar valores e combinar condições sem perder os limites.

Um programa toma decisões avaliando condições. `if` executa um bloco quando a condição é verdadeira. `elif` permite outra condição se as anteriores falharam. `else` cobre o caso restante. Somente o primeiro ramo verdadeiro de uma mesma cadeia é executado.

Comparações como `<`, `<=`, `>=` e `==` produzem booleanos. A diferença entre `<` e `<=` é importante no limite: se a aprovação começa em 7, a própria nota 7 precisa pertencer a essa faixa. Antes de programar, desenhe mentalmente intervalos sem buracos nem sobreposição.

`and` exige que duas condições sejam verdadeiras. `or` aceita que pelo menos uma seja verdadeira. `not` inverte uma condição. Parênteses podem tornar uma combinação mais fácil de ler. Evite comparar strings como `"True"` com o booleano `True`: são valores de tipos diferentes.

Uma função pode usar return dentro de um ramo. Ao executar return, a chamada termina imediatamente. Não esqueça de cobrir os demais caminhos: uma função que termina sem return devolve None, e isso pode não ser o contrato.

Na prática, as entradas estão dentro dos tipos e faixas especificados. Não há nota inválida escondida. Você precisa escolher corretamente as fronteiras e devolver strings exatas para os resultados. Os casos de 5 e 7 existem porque decisões erradas muitas vezes passam nos exemplos centrais e falham nos limites.

## Exemplo comentado

```python
def faixa_temperatura(temperatura):
    if temperatura < 15:
        return "frio"
    elif temperatura < 25:
        return "ameno"
    return "quente"
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo justificar cada valor exatamente na fronteira.
- [ ] Usei decisões legíveis e não respostas fixas para os exemplos.

Abra o [enunciado](../../../praticas/aula07_decisoes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula07_decisoes/pratica.py) e consulte o [teste público](../../../testes/test_aula07_decisoes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 07
```

```powershell
# Windows
py -3 estudar.py testar 07
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

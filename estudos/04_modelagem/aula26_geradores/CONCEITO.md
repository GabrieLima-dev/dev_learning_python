# 26 — Iteradores, geradores e processamento em lotes

**Objetivo:** Produzir valores sob demanda e agrupar entradas sem consumi-las antecipadamente.

Um iterável fornece elementos para uma repetição. Um iterador mantém a posição de consumo e entrega o próximo elemento por next. Quando termina, levanta StopIteration. Diferentemente de uma lista, um iterador comum não volta ao início depois de ser consumido.

Uma função com yield cria um gerador. Em vez de produzir toda a saída de uma vez, ela devolve um valor e suspende a execução, mantendo seu estado. A próxima solicitação retoma a partir desse ponto. Isso permite processar sequências grandes sem guardar todo o resultado na memória.

Uma consequência importante é que o corpo do gerador normalmente só começa a rodar no primeiro consumo. Uma validação colocada antes do primeiro yield, dentro da função, também pode ocorrer apenas nesse momento. Os testes desta aula aceitam a validação no momento de criar ou de consumir o iterador, e explicam essa possibilidade.

Processar em lotes agrupa uma quantidade limitada de elementos por vez. O último lote pode ser menor. Cada lote precisa ser uma lista independente: se você reutilizar e limpar a mesma lista depois de entregá-la, quem recebeu pode observar os dados desaparecendo.

A avaliação inclui um iterador que acusa consumo além do necessário. Esse caso torna a promessa de processamento gradual observável. Apenas devolver iter(lista_completa) não atende ao contrato de memória, mesmo que uma lista pequena tenha o resultado correto.

## Exemplo comentado

```python
def contagem_regressiva(inicio):
    atual = inicio
    while atual > 0:
        yield atual
        atual -= 1

sequencia = contagem_regressiva(3)
print(next(sequencia))  # 3
print(list(sequencia))  # [2, 1]
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo explicar quando o corpo do gerador começa a executar.
- [ ] Meu primeiro lote não exige consumir toda a entrada.

Abra o [enunciado](../../../praticas/aula26_geradores/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula26_geradores/pratica.py) e consulte o [teste público](../../../testes/test_aula26_geradores.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 26
```

```powershell
# Windows
py -3 estudar.py testar 26
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

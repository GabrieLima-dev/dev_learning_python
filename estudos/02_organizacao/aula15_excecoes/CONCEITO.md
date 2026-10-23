# 15 — Exceções e validação

**Objetivo:** Rejeitar entradas inválidas com tipos e mensagens previsíveis.

Uma exceção interrompe o fluxo normal quando algo impede a operação. ValueError normalmente indica um valor inadequado; TypeError costuma indicar um tipo inadequado. A mensagem ajuda a entender a causa, enquanto o tipo permite tratar uma categoria de problema.

`raise ValueError("mensagem")` comunica uma violação de regra. `try` e `except` permitem tratar uma falha esperada. Capture a exceção específica: um except muito amplo pode esconder um erro de programação que você deveria corrigir. Não transforme toda falha silenciosamente em zero.

É comum validar uma entrada antes de alterar dados. Se a regra rejeita um valor, o restante da operação não deve ocorrer. Assim, quem chama consegue corrigir a entrada e tentar outra vez sem lidar com um estado parcialmente alterado.

Converter texto e validar seu domínio são duas etapas diferentes. O texto pode representar um inteiro e, ainda assim, esse inteiro não ser uma idade válida para a aplicação. Decida qual mensagem corresponde a cada etapa. Nesta aula o contrato escolhe uma mensagem única para qualquer idade inválida, facilitando a interface para quem usa.

Nos testes, `assertRaises` verifica que uma exceção foi levantada. A ausência de exceção também faz o teste falhar. Quando a mensagem é parte do contrato, ela é comparada exatamente; devolver a mensagem como string não equivale a levantar ValueError.

## Exemplo comentado

```python
def raiz_de_contagem(valor):
    if valor < 0:
        raise ValueError("contagem negativa")
    return valor ** 0.5
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Capturei apenas a falha esperada de conversão.
- [ ] Diferencio levantar uma exceção de retornar um texto de erro.

Abra o [enunciado](../../../praticas/aula15_excecoes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula15_excecoes/pratica.py) e consulte o [teste público](../../../testes/test_aula15_excecoes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 15
```

```powershell
# Windows
py -3 estudar.py testar 15
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

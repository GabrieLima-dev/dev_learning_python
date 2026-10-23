# 06 — Entrada e saída no terminal

**Objetivo:** Ler entradas em ordem, converter números e imprimir a saída especificada.

`input()` lê uma linha digitada e devolve uma string sem a quebra de linha final. Se o aluno digita 25, o valor recebido é `"25"`. Para calcular com ele, primeiro converta para número. `print()` escreve uma representação no terminal e, por padrão, encerra a linha.

É possível passar uma mensagem para `input`, como `input("Cidade: ")`. Essa mensagem é parte da interação. Nesta prática, o contrato pede leituras sem mensagem para que o conteúdo da saída tenha um formato único. Você continuará sabendo o que digitar porque o enunciado descreve a ordem das leituras.

Nas aulas anteriores, as funções recebiam parâmetros e devolviam valores. Aqui vamos praticar uma função que conversa com o terminal. Ela recebe zero parâmetros, lê com input e escreve com print. Se não há `return` com valor, o Python devolve `None`, que representa a ausência de um valor de retorno.

Os testes substituem temporariamente input por respostas preparadas e capturam print. Você não precisa digitar durante um teste. Essa substituição se chama simulação; mais adiante você aprenderá a escrevê-la. O teste verifica também a quantidade de leituras, pois solicitar uma entrada extra deixaria uma pessoa esperando sem necessidade.

Evite executar input na raiz do arquivo. Coloque a interação dentro da função. Importar um módulo apenas para testar uma função não deve iniciar uma conversa. Para experimentar manualmente, use os comandos da prática, que importam e chamam uma função de propósito.

## Exemplo comentado

```python
def perguntar_cidade():
    cidade = input()
    print(f"Cidade escolhida: {cidade}")

# A definição acima não executa a função automaticamente.
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] As entradas ficam dentro de funções e importar o módulo não pede digitação.
- [ ] Sei por que o teste captura a saída em vez de procurar uma soma no return.

Abra o [enunciado](../../../praticas/aula06_entrada_saida/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula06_entrada_saida/pratica.py) e consulte o [teste público](../../../testes/test_aula06_entrada_saida.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 06
```

```powershell
# Windows
py -3 estudar.py testar 06
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

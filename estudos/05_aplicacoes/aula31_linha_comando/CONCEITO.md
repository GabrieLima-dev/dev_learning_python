# 31 — Aplicações de linha de comando

**Objetivo:** Criar uma calculadora de terminal com ajuda, validação e códigos de saída.

Uma aplicação de linha de comando recebe argumentos na execução. Eles são diferentes de input: o usuário escreve a operação e os dados junto com o comando, sem uma conversa posterior. O módulo argparse interpreta opções, argumentos posicionais e mensagens de ajuda.

ArgumentParser representa a interface. `add_argument` define os argumentos. `choices` restringe opções, `type=int` converte números e `nargs="+"` exige um ou mais valores. `parse_args` usa os argumentos fornecidos ou os da execução do processo quando recebe None.

Erros de uso, como uma opção desconhecida, fazem argparse escrever ajuda resumida em stderr e levantar SystemExit com código 2. Saída normal vai para stdout. Um código de saída zero indica sucesso para outros programas. Não é necessário implementar manualmente essas convenções quando a biblioteca já as oferece.

Separar main(argv=None) permite usar a mesma interface no terminal e nos testes. Um teste passa uma lista de argumentos diretamente e captura a saída. O bloco de execução `raise SystemExit(main())` transforma o código retornado em status do processo.

Para executar um módulo dentro de pacotes, use `python3 -m caminho.do.modulo`. Isso mantém a raiz do projeto como base dos imports. Executar um arquivo interno por caminho pode mudar essa base e causar dificuldades desnecessárias.

O contrato especifica o que será impresso, pois uma interface de terminal também é observável por scripts. Nesta prática não há prompts nem banners: os argumentos contêm toda a entrada.

## Exemplo comentado

```python
import argparse

parser = argparse.ArgumentParser(description="Mostra uma palavra")
parser.add_argument("palavra")
# Em uma execução real: argumentos = parser.parse_args()
argumentos = parser.parse_args(["olá"])
print(argumentos.palavra)
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Separei o parser, a execução e o bloco de entrada.
- [ ] Sei distinguir stdout, stderr e código de saída.

Abra o [enunciado](../../../praticas/aula31_linha_comando/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula31_linha_comando/pratica.py) e consulte o [teste público](../../../testes/test_aula31_linha_comando.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 31
```

```powershell
# Windows
py -3 estudar.py testar 31
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

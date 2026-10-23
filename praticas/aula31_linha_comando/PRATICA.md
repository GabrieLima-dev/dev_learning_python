# Prática 31 — Aplicações de linha de comando

**Objetivo:** Criar uma calculadora de terminal com ajuda, validação e códigos de saída.

Leia primeiro o [conceito](../../estudos/05_aplicacoes/aula31_linha_comando/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`criar_parser()`: devolve ArgumentParser com argumento posicional `operacao`, aceitando `somar` ou `maior`, e argumento `numeros`, aceitando um ou mais int. Descrição e texto completo da ajuda são livres.

`main(argv=None)`: usa o parser, soma ou encontra o maior número e imprime apenas esse inteiro seguido de quebra de linha. Retorna int 0 em sucesso. Sem números, com operação inválida ou número não inteiro, deixe argparse levantar SystemExit(2) e escrever erro em stderr. `--help` levanta SystemExit(0) e escreve ajuda em stdout. Não use input.

Depois de implementar: `python3 -m praticas.aula31_linha_comando.pratica somar 2 -3 8` imprime 7. No Windows use `py -3 -m ...`. O bloco de entrada já está fornecido.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A31-01 | Parser interpreta ["somar", "2", "-3"] como operacao="somar", numeros=[2, -3]. |
| A31-02 | main(["somar", "2", "-3", "8"]) → código 0, stdout "7\n" e stderr vazio. |
| A31-03 | main(["maior", "-8", "-2", "-5"]) → 0 e stdout "-2\n". |
| A31-04 | Sem números, operação "outra" ou número "x" → SystemExit(2), stderr não vazio. |
| A31-05 | --help → SystemExit(0), ajuda em stdout. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 31
```

```powershell
# Windows
py -3 estudar.py testar 31
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula31_linha_comando -v` (Windows: `py -3 -m unittest testes.test_aula31_linha_comando -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A31-NN nesta tabela e [o código do teste](../../testes/test_aula31_linha_comando.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Separei o parser, a execução e o bloco de entrada.
- [ ] Sei distinguir stdout, stderr e código de saída.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

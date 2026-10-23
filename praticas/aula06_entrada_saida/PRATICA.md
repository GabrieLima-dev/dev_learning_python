# Prática 06 — Entrada e saída no terminal

**Objetivo:** Ler entradas em ordem, converter números e imprimir a saída especificada.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula06_entrada_saida/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`cumprimentar()`: lê uma vez usando `input()` sem argumento, remove espaços das extremidades do nome e imprime `Olá, NOME!` seguido de uma quebra de linha. Nome vazio é permitido. Retorna `None`.

`somar_entradas()`: lê duas vezes com `input()` sem argumento; ambas as entradas representam inteiros válidos. Imprime a soma como inteiro seguida de quebra de linha. Não imprime rótulo. Retorna `None`.

Experimento manual, a partir da raiz: `python3 -c "from praticas.aula06_entrada_saida.pratica import cumprimentar; cumprimentar()"`. No Windows, troque `python3` por `py -3`. Digite seu nome e pressione Enter. Importar o arquivo sozinho não deve ler nem imprimir.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A06-01 | Entrada " Ana " → saída "Olá, Ana!\n", uma leitura sem argumento e retorno None. |
| A06-02 | Entrada vazia → saída "Olá, !\n". |
| A06-03 | Entradas "2" e "3" → saída "5\n", exatamente duas leituras sem argumentos. |
| A06-04 | Entradas " -4 " e "4" → saída "0\n". |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 06
```

```powershell
# Windows
py -3 estudar.py testar 06
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula06_entrada_saida -v` (Windows: `py -3 -m unittest testes.test_aula06_entrada_saida -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A06-NN nesta tabela e [o código do teste](../../testes/test_aula06_entrada_saida.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] As entradas ficam dentro de funções e importar o módulo não pede digitação.
- [ ] Sei por que o teste captura a saída em vez de procurar uma soma no return.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

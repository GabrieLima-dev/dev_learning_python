# Prática 20 — CSV e intercâmbio de tabelas

**Objetivo:** Exportar e importar produtos sem quebrar campos com vírgulas ou aspas.

Leia primeiro o [conceito](../../estudos/03_persistencia/aula20_csv/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`exportar_produtos(caminho, produtos)`: grava CSV UTF-8 usando vírgula e cabeçalho exato, na ordem `nome,preco_centavos`. Cada produto tem nome string e preco_centavos int não negativo. Sobrescreve arquivo, preserva lista e registros, retorna None. Lista vazia ainda grava o cabeçalho.

`importar_produtos(caminho)`: lê arquivo existente nesse formato e retorna lista de dicts com nome str e preco_centavos int, preservando ordem de linhas. Arquivo só com cabeçalho retorna []. Nomes podem conter acento, vírgula, aspas e quebra de linha. Diretório pai existe. Não há linhas ou cabeçalhos inválidos nos testes.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A20-01 | Exporta "Café, moído"/1200 e nome com aspas e quebra de linha/0; leitura CSV confirma cabeçalho, campos e preservação. |
| A20-02 | Exportar [] substitui arquivo anterior e produz só o cabeçalho. |
| A20-03 | Importa CSV escrito pelo teste com vírgula, aspas, quebra e acento; preços voltam como int. |
| A20-04 | Arquivo só com cabeçalho → []. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 20
```

```powershell
# Windows
py -3 estudar.py testar 20
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula20_csv -v` (Windows: `py -3 -m unittest testes.test_aula20_csv -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A20-NN nesta tabela e [o código do teste](../../testes/test_aula20_csv.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Usei o módulo csv para lidar com campos especiais.
- [ ] Abri os arquivos com UTF-8 e newline apropriado.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

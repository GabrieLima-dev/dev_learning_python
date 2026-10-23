# Prática 18 — Arquivos de texto e caminhos

**Objetivo:** Salvar e recuperar linhas de texto usando caminhos recebidos como argumento.

Leia primeiro o [conceito](../../estudos/03_persistencia/aula18_arquivos/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`salvar_linhas(caminho, linhas)`: caminho é str ou Path e seu diretório pai existe. Linhas é lista de strings sem quebras internas. Sobrescreva o arquivo em UTF-8, com uma quebra `\n` depois de cada linha, inclusive a última. Lista vazia cria arquivo vazio. Retorne None e preserve linhas.

`ler_linhas(caminho)`: leia UTF-8 e devolva lista de strings sem as quebras de linha, preservando linhas vazias e espaços dentro delas. Arquivo vazio ou inexistente retorna []. Os arquivos de teste usam `\n` e terminam ou não em uma quebra final. Outros erros de acesso devem se propagar; não são simulados nesta aula.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A18-01 | Salvar ["Olá", "", " fim "] escreve exatamente "Olá\n\n fim \n" em UTF-8, preserva lista e retorna None. |
| A18-02 | Salvar [] usando caminho str apaga conteúdo antigo e deixa arquivo vazio. |
| A18-03 | Ler "Olá\n\n fim \n" e a variante sem quebra final → ["Olá", "", " fim "]. |
| A18-04 | Ler arquivo ausente e arquivo vazio → []; ausência não cria arquivo. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 18
```

```powershell
# Windows
py -3 estudar.py testar 18
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula18_arquivos -v` (Windows: `py -3 -m unittest testes.test_aula18_arquivos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A18-NN nesta tabela e [o código do teste](../../testes/test_aula18_arquivos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] O caminho vem do argumento e não está fixado na minha máquina.
- [ ] Sei por que devo escolher UTF-8 e distinguir arquivo ausente de outros erros.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

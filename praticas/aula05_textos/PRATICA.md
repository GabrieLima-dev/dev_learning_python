# Prática 05 — Textos e formatação

**Objetivo:** Transformar textos e produzir uma mensagem com formato exato.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula05_textos/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`normalizar_usuario(texto)`: recebe string; retorna string com extremidades em branco removidas e letras em minúsculas. Preserva espaços internos e acentos. Entrada vazia ou só espaços resulta em string vazia.

`etiqueta(produto, quantidade)`: recebe string e inteiro não negativo; retorna exatamente `Item: PRODUTO (QUANTIDADE)`, substituindo os dois valores. Não altera o produto, não acrescenta quebra de linha e não imprime.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A05-01 | normalizar_usuario("  ANA  ") → "ana". |
| A05-02 | normalizar_usuario("  JOÃO SILVA ") → "joão silva". |
| A05-03 | String vazia e "   " → "". |
| A05-04 | etiqueta("Livro", 2) → "Item: Livro (2)". |
| A05-05 | etiqueta(" Chá ", 0) → "Item:  Chá  (0)"; espaços do produto são preservados. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 05
```

```powershell
# Windows
py -3 estudar.py testar 05
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula05_textos -v` (Windows: `py -3 -m unittest testes.test_aula05_textos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A05-NN nesta tabela e [o código do teste](../../testes/test_aula05_textos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Sei que os métodos de string devolvem um novo valor.
- [ ] Conferi os espaços, a pontuação e o comportamento com texto vazio.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

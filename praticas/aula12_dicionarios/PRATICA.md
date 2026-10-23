# Prática 12 — Dicionários e agregação

**Objetivo:** Contar ocorrências e calcular valores a partir de registros.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula12_dicionarios/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`contar_votos(votos)`: recebe lista de strings não vazias; retorna dict com cada texto exato como chave e sua contagem inteira. Distingue maiúsculas e acentos. Lista vazia retorna {}. A ordem das chaves não faz parte da comparação.

`valor_estoque(produtos)`: recebe lista de dicts, cada um com `preco_centavos` e `quantidade`, ambos inteiros não negativos. Retorna int com a soma dos preços multiplicados pelas respectivas quantidades. Lista vazia retorna 0. Não altere as entradas.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A12-01 | ["Ana", "Bia", "Ana", "ana"] → {"Ana": 2, "Bia": 1, "ana": 1}. |
| A12-02 | contar_votos([]) → {}. |
| A12-03 | Estoque com (150, 2) e (900, 1) → 1200; preserva registros. |
| A12-04 | Estoque vazio → 0; produto de preço 100 e quantidade 0 → 0. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 12
```

```powershell
# Windows
py -3 estudar.py testar 12
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula12_dicionarios -v` (Windows: `py -3 -m unittest testes.test_aula12_dicionarios -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A12-NN nesta tabela e [o código do teste](../../testes/test_aula12_dicionarios.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo explicar o valor padrão para uma chave nova.
- [ ] Não alterei os registros recebidos.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

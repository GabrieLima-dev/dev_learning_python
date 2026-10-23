# Prática 17 — Checkpoint: resumo de vendas

**Objetivo:** Consolidar registros em um relatório sem perder dados nem aceitar valores inválidos.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula17_checkpoint_colecoes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`resumir_vendas(vendas)`: recebe lista de dicts com `produto` (string não vazia), `quantidade` (int) e `preco_centavos` (int). Para cada produto, retorna um dict interno com `quantidade` total e `receita_centavos` total. Exemplo de resultado: `{"Livro": {"quantidade": 2, "receita_centavos": 1000}}`.

Produto diferencia maiúsculas; não normalize. Quantidade deve ser maior que zero e preço pode ser zero. Caso quantidade <= 0 ou preço < 0, levante `ValueError("venda inválida")`. Todos os campos e tipos estão presentes e corretos. Entrada vazia retorna {}. Preserve a lista e todos os seus dicts, inclusive em caso de erro.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A17-01 | Entrada vazia → {}. |
| A17-02 | Livro: 2×500 e 1×700; Caneta: 3×100 → Livro quantidade 3/receita 1700 e Caneta 3/300; preserva entrada. |
| A17-03 | Produtos "A" e "a" são separados; preço zero é aceito. |
| A17-04 | Quantidade 0, quantidade -1 ou preço -1 → ValueError: venda inválida; entrada permanece intacta mesmo após venda válida. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 17
```

```powershell
# Windows
py -3 estudar.py testar 17
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula17_checkpoint_colecoes -v` (Windows: `py -3 -m unittest testes.test_aula17_checkpoint_colecoes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A17-NN nesta tabela e [o código do teste](../../testes/test_aula17_checkpoint_colecoes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Calculei a receita por venda, inclusive quando o preço muda.
- [ ] Sei explicar como evitei modificar os dados de entrada.
- [ ] Revisei meu commit e sincronizei minha cópia no GitHub, se configurada.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

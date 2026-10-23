# Prática 24 — Dataclasses e composição de objetos

**Objetivo:** Representar itens imutáveis e compor um carrinho com estado independente.

Leia primeiro o [conceito](../../estudos/04_modelagem/aula24_composicao/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

Implemente `Item` como dataclass congelada com campos, nesta ordem: `nome: str`, `preco_centavos: int`, `quantidade: int = 1`. Entradas são válidas: nome não vazio, preço não negativo, quantidade positiva. Método `subtotal()` retorna int preço vezes quantidade. A igualdade entre itens usa os valores dos campos.

`Carrinho()`: começa vazio. `adicionar(item)` armazena o Item recebido no carrinho e retorna None. `total()` retorna int com a soma dos subtotais, ou 0 se vazio. Adicionar duas vezes o mesmo item conta duas vezes. Carrinhos não compartilham a lista. A prática exige usar os métodos subtotal dos itens; os testes verificam os totais e a dataclass congelada, e a composição é revisada no checklist.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A24-01 | Item("Livro", 500) tem quantidade 1 e subtotal 500; Item("Caneta", 100, 3) tem subtotal 300. |
| A24-02 | Item é dataclass, igualdade compara campos, e alterar quantidade levanta FrozenInstanceError. |
| A24-03 | Carrinho vazio → 0; adicionar Livro/500 e Caneta/100×3 → 800; adicionar Livro novamente → 1300. |
| A24-04 | Adicionar item de valor 10 a um carrinho mantém outro em 0. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 24
```

```powershell
# Windows
py -3 estudar.py testar 24
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula24_composicao -v` (Windows: `py -3 -m unittest testes.test_aula24_composicao -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A24-NN nesta tabela e [o código do teste](../../testes/test_aula24_composicao.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Usei a dataclass para representar dados e o carrinho para coordenar itens.
- [ ] O carrinho usa subtotal dos itens e cada carrinho tem sua coleção.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

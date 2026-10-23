# Prática 16 — Módulos, pacotes e anotações de tipo

**Objetivo:** Distribuir uma regra e sua composição entre dois módulos.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula16_modulos/CONCEITO.md). Edite [pratica.py](pratica.py) e [operacoes.py](operacoes.py).

## Contrato da atividade

Em `operacoes.py`, implemente `subtotal(preco: int, quantidade: int) -> int`, multiplicando inteiros não negativos.

Em `pratica.py`, implemente `total(itens: list[tuple[int, int]]) -> int`. Cada tupla contém preço em centavos e quantidade, nessa ordem. Some os subtotais, preserve itens e retorne 0 para lista vazia. Use a função do módulo operacoes. Um teste substitui essa função por uma simulação e verifica a colaboração: por isso use o import de módulo já fornecido e chame `operacoes.subtotal`, uma vez por item, na ordem recebida. Essa exigência é visível, faz parte da aula e não é um detalhe escondido.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A16-01 | subtotal(125, 3) → 375; subtotal(100, 0) → 0. |
| A16-02 | total([(100, 2), (50, 3)]) → 350, entrada preservada. |
| A16-03 | total([]) → 0. |
| A16-04 | Delegação: subtotal simulado devolve 11 e 22; total retorna 33 e chama com (100, 2), depois (50, 3). |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 16
```

```powershell
# Windows
py -3 estudar.py testar 16
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula16_modulos -v` (Windows: `py -3 -m unittest testes.test_aula16_modulos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A16-NN nesta tabela e [o código do teste](../../testes/test_aula16_modulos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Minha importação não executa interação ou escrita em arquivo.
- [ ] Consigo explicar por que a anotação não valida o valor em tempo de execução.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

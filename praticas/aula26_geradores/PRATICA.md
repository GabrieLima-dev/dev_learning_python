# Prática 26 — Iteradores, geradores e processamento em lotes

**Objetivo:** Produzir valores sob demanda e agrupar entradas sem consumi-las antecipadamente.

Leia primeiro o [conceito](../../estudos/04_modelagem/aula26_geradores/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`pares_ate(limite)`: recebe int não negativo; retorna um iterador (iter(resultado) é o próprio resultado) que produz pares de 0 até limite, inclusive quando par. Depois de consumido, fica esgotado.

`lotes(iteravel, tamanho)`: tamanho é int positivo. Retorna iterador de listas com até tamanho elementos, preservando ordem. Último lote incompleto é permitido e não há lote vazio. Cada lista é independente. Não consuma o iterável ao criar o resultado nem leia além do lote solicitado: ao pedir o primeiro lote de tamanho 2, apenas dois itens podem ser consumidos. Tamanho <= 0 levanta `ValueError("tamanho deve ser positivo")`, na criação ou no primeiro consumo.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A26-01 | pares_ate(5) é iterador, produz [0, 2, 4] e depois []; limite 0 → [0], limite 6 → [0, 2, 4, 6]. |
| A26-02 | lotes(iter([1, 2, 3, 4, 5]), 2) → [[1, 2], [3, 4], [5]]; listas independentes. |
| A26-03 | lotes([], 2) → []; lotes([1, 2], 1) → [[1], [2]]. |
| A26-04 | Tamanhos 0 e -1 → ValueError: tamanho deve ser positivo. |
| A26-05 | Criar lotes não consome entrada; pedir primeiro lote de 2 consome exatamente [10, 20], sem buscar terceiro. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 26
```

```powershell
# Windows
py -3 estudar.py testar 26
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula26_geradores -v` (Windows: `py -3 -m unittest testes.test_aula26_geradores -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A26-NN nesta tabela e [o código do teste](../../testes/test_aula26_geradores.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo explicar quando o corpo do gerador começa a executar.
- [ ] Meu primeiro lote não exige consumir toda a entrada.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

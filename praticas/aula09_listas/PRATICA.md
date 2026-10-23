# Prática 09 — Listas e preservação dos dados

**Objetivo:** Filtrar e reorganizar listas sem alterar os argumentos.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula09_listas/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`selecionar_positivos(valores)`: recebe lista de inteiros e retorna nova lista apenas com os maiores que zero. Preserva ordem e repetições; zero não entra.

`rotacionar(valores)`: recebe lista de inteiros e retorna nova lista em que o último elemento passa para o início e os demais avançam uma posição. Lista vazia resulta em nova lista vazia. Lista com um item mantém esse item. Nenhuma função pode alterar a lista recebida nem devolvê-la como o próprio objeto de resultado.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A09-01 | [-2, 3, 0, 3, 1] → positivos [3, 3, 1]; entrada preservada e resultado novo. |
| A09-02 | Positivos de [] e de [-1, 0] → novas listas vazias. |
| A09-03 | Rotação de [1, 2, 3] → [3, 1, 2]; entrada preservada. |
| A09-04 | Rotação de [] e [8] → cópias com os mesmos valores. |
| A09-05 | Rotação de [2, 2, 7, 2] → [2, 2, 2, 7]. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 09
```

```powershell
# Windows
py -3 estudar.py testar 09
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula09_listas -v` (Windows: `py -3 -m unittest testes.test_aula09_listas -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A09-NN nesta tabela e [o código do teste](../../testes/test_aula09_listas.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Sei distinguir copiar uma lista de atribuí-la a outro nome.
- [ ] Minhas funções preservam a entrada e funcionam com lista vazia.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

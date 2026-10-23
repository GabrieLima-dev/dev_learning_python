# Prática 11 — Tuplas, conjuntos e desempacotamento

**Objetivo:** Escolher estruturas conforme ordem, posição e duplicação.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula11_tuplas_conjuntos/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`coordenadas(texto)`: recebe exatamente dois números válidos separados por uma vírgula, com espaços opcionais, usando ponto decimal. Retorna tupla de dois floats na mesma ordem. Não é necessário validar texto inválido.

`comuns(a, b)`: recebe duas listas de inteiros; retorna lista crescente, sem repetição, dos valores presentes em ambas. Não altera as entradas. Listas vazias são permitidas.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A11-01 | coordenadas("2,3") → tupla (2.0, 3.0). |
| A11-02 | coordenadas(" -2.5, 0 ") → (-2.5, 0.0). |
| A11-03 | comuns([3, 1, 3, 2], [3, 2, 2]) → [2, 3], sem mudar entradas. |
| A11-04 | comuns([], [1]) e comuns([1], [2]) → []. |
| A11-05 | comuns([-1, 0, -1], [0, -1]) → [-1, 0]. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 11
```

```powershell
# Windows
py -3 estudar.py testar 11
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula11_tuplas_conjuntos -v` (Windows: `py -3 -m unittest testes.test_aula11_tuplas_conjuntos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A11-NN nesta tabela e [o código do teste](../../testes/test_aula11_tuplas_conjuntos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Sei explicar por que o conjunto não é a saída final ordenada.
- [ ] Usei uma tupla para o par de coordenadas.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

# Prática 15 — Exceções e validação

**Objetivo:** Rejeitar entradas inválidas com tipos e mensagens previsíveis.

Leia primeiro o [conceito](../../estudos/02_organizacao/aula15_excecoes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`dividir(a, b)`: recebe int ou float. Se b for zero, levanta `ValueError("divisor não pode ser zero")`. Caso contrário, retorna float a / b. Não é necessário aceitar textos.

`ler_idade(texto)`: recebe string. Converte com int e aceita somente valores de 0 a 130, inclusive. Retorna int. Qualquer texto que int rejeite, ou número fora da faixa, deve levantar `ValueError("idade inválida")`. Espaços nas extremidades são aceitos. O teste confere a mensagem exata, com acentos.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A15-01 | dividir(7, 2) → 3.5; dividir(-4, 2) → -2.0. |
| A15-02 | dividir(1, 0) e dividir(0, 0) → ValueError: divisor não pode ser zero. |
| A15-03 | ler_idade(" 18 "), "0" e "130" → 18, 0 e 130. |
| A15-04 | Idades "", "abc", "2.5", "-1" e "131" → ValueError: idade inválida. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 15
```

```powershell
# Windows
py -3 estudar.py testar 15
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula15_excecoes -v` (Windows: `py -3 -m unittest testes.test_aula15_excecoes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A15-NN nesta tabela e [o código do teste](../../testes/test_aula15_excecoes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Capturei apenas a falha esperada de conversão.
- [ ] Diferencio levantar uma exceção de retornar um texto de erro.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

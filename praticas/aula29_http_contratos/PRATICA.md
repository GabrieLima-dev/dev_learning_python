# Prática 29 — HTTP, URLs e contratos de resposta

**Objetivo:** Codificar parâmetros de URL e interpretar respostas segundo um contrato explícito.

Leia primeiro o [conceito](../../estudos/05_aplicacoes/aula29_http_contratos/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`montar_url(base, parametros)`: base é URL sem consulta e sem fragmento; parametros é dict de strings para strings. Retorne base se vazio; caso contrário acrescente ? e consulta codificada com urlencode. Ordem dos parâmetros é livre. Preserve o dict.

`interpretar_resposta(status, corpo)`: status é int e corpo é string. Status 200: devolva o valor de json.loads, qualquer tipo JSON; sintaxe inválida propaga JSONDecodeError. Status 404: retorne None sem interpretar o corpo. Qualquer outro status: levante `RuntimeError("HTTP N")`, com N substituído pelo código, também sem interpretar corpo. Não faça requisições de rede.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A29-01 | Parâmetros {q:"café & pão", pagina:"2"} voltam íntegros ao decodificar a URL; base preservada. |
| A29-02 | Parâmetros vazios → base exata, sem ?. |
| A29-03 | 200 com objeto, lista e null devolve dict, list e None correspondentes. |
| A29-04 | 200 com "{" → JSONDecodeError; 404 com texto não JSON → None. |
| A29-05 | Códigos 201, 400 e 500 → RuntimeError: HTTP 201, HTTP 400 e HTTP 500, respectivamente. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 29
```

```powershell
# Windows
py -3 estudar.py testar 29
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula29_http_contratos -v` (Windows: `py -3 -m unittest testes.test_aula29_http_contratos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A29-NN nesta tabela e [o código do teste](../../testes/test_aula29_http_contratos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Codifiquei os parâmetros com a biblioteca em vez de concatenar os valores.
- [ ] Sei distinguir erro de status e erro de sintaxe do corpo.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

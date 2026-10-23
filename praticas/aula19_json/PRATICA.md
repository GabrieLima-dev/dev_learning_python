# Prática 19 — JSON e dados estruturados

**Objetivo:** Persistir configurações e distinguir ausência, sintaxe inválida e formato inválido.

Leia primeiro o [conceito](../../estudos/03_persistencia/aula19_json/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`salvar_config(caminho, config)`: recebe str ou Path e dict com chaves strings e valores JSON compatíveis. Sobrescreve em UTF-8 com JSON equivalente ao dict, retorna None e preserva config. O diretório pai existe. Indentação, ordem de chaves e escape de acentos são livres.

`carregar_config(caminho)`: retorna o dict lido. Ausente retorna {} sem criar arquivo. JSON malformado propaga `json.JSONDecodeError` (mensagem livre). JSON válido cujo topo não é dict levanta `ValueError("configuração deve ser objeto")`. Não altere um arquivo rejeitado.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A19-01 | Salvar {"tema": "claro", "nome": "João", "avisos": True} preserva dados e substitui arquivo antigo por JSON equivalente. |
| A19-02 | Carregar objeto {"n": 2, "itens": [1, None]} devolve esse dict. |
| A19-03 | Arquivo ausente → {}, sem criar arquivo. |
| A19-04 | Conteúdo "{" → JSONDecodeError; arquivo é preservado. |
| A19-05 | JSON [], null e 3 → ValueError: configuração deve ser objeto. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 19
```

```powershell
# Windows
py -3 estudar.py testar 19
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula19_json -v` (Windows: `py -3 -m unittest testes.test_aula19_json -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A19-NN nesta tabela e [o código do teste](../../testes/test_aula19_json.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Uso json em vez de avaliar o texto como código.
- [ ] Diferencio arquivo ausente, JSON malformado e JSON com tipo inadequado.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

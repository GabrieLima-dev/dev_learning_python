# Prática 22 — Checkpoint: diário de eventos em JSON

**Objetivo:** Registrar eventos acumulativos com validação e preservação do arquivo em erros previstos.

Leia primeiro o [conceito](../../estudos/03_persistencia/aula22_checkpoint_persistencia/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`listar_eventos(caminho)`: devolve a lista guardada em JSON UTF-8. Arquivo ausente retorna [] sem criá-lo. JSON malformado propaga JSONDecodeError. JSON cujo topo não é list levanta `ValueError("histórico deve ser lista")`. Os elementos de uma lista já existente são válidos; não é necessário revalidá-los.

`registrar_evento(caminho, evento)`: evento é dict que deve conter exatamente as chaves `tipo` e `descricao`, ambas strings que, após strip, não ficam vazias. Caso contrário levanta `ValueError("evento inválido")` sem criar nem alterar o arquivo. Para válido, registre uma cópia com os dois textos sem espaços nas extremidades, no fim do histórico; preserve evento e devolva int com a nova quantidade de eventos. Se a leitura do histórico falhar, propague a exceção sem reescrever o arquivo. O diretório pai existe.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A22-01 | Histórico ausente → [] sem criar arquivo. |
| A22-02 | Registrar {tipo:" estudo ", descricao:" Python "} retorna 1; segundo evento retorna 2; preserva entrada e ordem no JSON. |
| A22-03 | Evento {}, tipo vazio, descrição numérica ou chave extra → ValueError: evento inválido; arquivo anterior intacto. |
| A22-04 | Evento inválido em caminho inexistente não cria arquivo. |
| A22-05 | Histórico "{" causa JSONDecodeError; histórico "{}" causa ValueError: histórico deve ser lista; registrar preserva ambos. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 22
```

```powershell
# Windows
py -3 estudar.py testar 22
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula22_checkpoint_persistencia -v` (Windows: `py -3 -m unittest testes.test_aula22_checkpoint_persistencia -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A22-NN nesta tabela e [o código do teste](../../testes/test_aula22_checkpoint_persistencia.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo explicar os caminhos de primeira escrita, acréscimo e falha.
- [ ] Nenhum erro previsto destrói um histórico anterior.
- [ ] Revisei meu commit e sincronizei minha cópia no GitHub, se configurada.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

# Prática 02 — Git e registro da evolução

**Objetivo:** Reconhecer os comandos de inspeção e começar a registrar sua evolução.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula02_git/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

Preencha quatro constantes do tipo `str`: `COMANDO_ESTADO` com `git status`; `COMANDO_DIFERENCAS` com `git diff`; `COMANDO_PREPARADO` com `git diff --staged`; `PASTA_LOCAL` com `.learning/`. Use exatamente esses textos, sem espaços extras. Este exercício verifica reconhecimento, não executa comandos.

Roteiro manual: na raiz do clone, execute os três comandos. Explique para si a diferença entre alterações preparadas e não preparadas. Após os testes verdes, use `git add praticas/aula02_git/pratica.py`, confira `git diff --staged` e faça `git commit -m "Conclui pratica inicial de Git"`. Se Git pedir identidade, configure seu próprio nome e e-mail conforme `docs/GIT.md`. Não copie dados pessoais de exemplos.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A02-01 | COMANDO_ESTADO é `"git status"`. |
| A02-02 | COMANDO_DIFERENCAS é `"git diff"`. |
| A02-03 | COMANDO_PREPARADO é `"git diff --staged"`. |
| A02-04 | PASTA_LOCAL é `".learning/"`. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 02
```

```powershell
# Windows
py -3 estudar.py testar 02
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula02_git -v` (Windows: `py -3 -m unittest testes.test_aula02_git -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A02-NN nesta tabela e [o código do teste](../../testes/test_aula02_git.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Executei status e diff e sei explicar a saída.
- [ ] Sei que commit é local e push envia para o remoto.
- [ ] Revisei os arquivos preparados e registrei uma mudança pequena na minha cópia.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

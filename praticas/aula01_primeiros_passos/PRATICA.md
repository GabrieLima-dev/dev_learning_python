# Prática 01 — Primeiros passos e leitura de testes

**Objetivo:** Escrever sua primeira função e reconhecer uma execução de teste bem-sucedida.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula01_primeiros_passos/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

Implemente `mensagem_inicial()` sem parâmetros. Ela deve **devolver** a string exata `Minha jornada em Python começou!`, incluindo acento, maiúscula e ponto de exclamação. Não adicione espaços nem quebra de linha ao retorno. A função não deve imprimir nada nem solicitar entrada. Você pode chamá-la várias vezes; o resultado deve ser sempre o mesmo.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A01-01 | Devolve exatamente `"Minha jornada em Python começou!"` como string. |
| A01-02 | Duas chamadas devolvem o mesmo texto e não escrevem no terminal. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 01
```

```powershell
# Windows
py -3 estudar.py testar 01
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula01_primeiros_passos -v` (Windows: `py -3 -m unittest testes.test_aula01_primeiros_passos -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A01-NN nesta tabela e [o código do teste](../../testes/test_aula01_primeiros_passos.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Sei distinguir o editor do terminal.
- [ ] Consigo explicar por que return e print produzem resultados diferentes.
- [ ] Executei os testes antes e depois de implementar.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

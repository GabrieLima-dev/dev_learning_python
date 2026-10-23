# Prática 07 — Decisões e expressões booleanas

**Objetivo:** Classificar valores e combinar condições sem perder os limites.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula07_decisoes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`classificar_nota(nota)`: recebe int ou float entre 0 e 10. Devolve `reprovado` se menor que 5; `recuperacao` se maior ou igual a 5 e menor que 7; `aprovado` se maior ou igual a 7. Os textos não possuem acentos.

`pode_entrar(idade, acompanhado)`: idade é inteiro não negativo, acompanhado é bool. Retorna bool: pode entrar se tem pelo menos 18 anos OU se tem pelo menos 12 anos e está acompanhado. Menores de 12 nunca entram.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A07-01 | Notas 0 e 4.99 → "reprovado". |
| A07-02 | Notas 5 e 6.99 → "recuperacao". |
| A07-03 | Notas 7 e 10 → "aprovado". |
| A07-04 | Idade 11, com ou sem acompanhante → False. |
| A07-05 | Idades 12 e 17: acompanhado → True; sozinho → False. |
| A07-06 | Idades 18 e 80, com ou sem acompanhante → True. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 07
```

```powershell
# Windows
py -3 estudar.py testar 07
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula07_decisoes -v` (Windows: `py -3 -m unittest testes.test_aula07_decisoes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A07-NN nesta tabela e [o código do teste](../../testes/test_aula07_decisoes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo justificar cada valor exatamente na fronteira.
- [ ] Usei decisões legíveis e não respostas fixas para os exemplos.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

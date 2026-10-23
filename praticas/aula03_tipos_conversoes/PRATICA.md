# Prática 03 — Variáveis, tipos e conversões

**Objetivo:** Converter entradas textuais e distinguir números, textos e booleanos.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula03_tipos_conversoes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`dobrar(texto)`: recebe uma string aceita por `int`, inclusive sinal negativo e espaços nas extremidades; devolve um `int` igual ao dobro. Não precisa tratar texto inválido.

`eh_python(texto)`: recebe uma string e devolve o `bool` `True` somente quando ela é exatamente `Python`. A comparação diferencia maiúsculas e espaços. Não normalize a entrada.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A03-01 | dobrar("12") → inteiro 24. |
| A03-02 | dobrar(" -3 ") → inteiro -6. |
| A03-03 | dobrar("0") → inteiro 0. |
| A03-04 | eh_python("Python") → True. |
| A03-05 | eh_python("python"), eh_python(" Python") e eh_python("") → False. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 03
```

```powershell
# Windows
py -3 estudar.py testar 03
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula03_tipos_conversoes -v` (Windows: `py -3 -m unittest testes.test_aula03_tipos_conversoes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A03-NN nesta tabela e [o código do teste](../../testes/test_aula03_tipos_conversoes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Consigo explicar a diferença entre "12" e 12.
- [ ] Minhas funções devolvem int e bool, conforme o contrato.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

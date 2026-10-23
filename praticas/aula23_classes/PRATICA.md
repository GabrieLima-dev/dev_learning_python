# Prática 23 — Classes, objetos e estado

**Objetivo:** Implementar uma conta com estado independente e validações antes de movimentar.

Leia primeiro o [conceito](../../estudos/04_modelagem/aula23_classes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`Conta(titular, saldo=0)`: titular é string não vazia e saldo é int em centavos. Guarda atributos públicos `titular` e `saldo`. Saldo inicial negativo levanta `ValueError("saldo inválido")`; zero é válido.

`depositar(valor)` e `sacar(valor)`: valor é int. Ambos rejeitam valor <= 0 com `ValueError("valor deve ser positivo")`. Sacar acima do saldo levanta `ValueError("saldo insuficiente")`. Em sucesso, atualizam saldo e retornam o novo saldo como int. Em erro, mantêm o saldo. Sacar exatamente o saldo é permitido. Instâncias têm estados independentes; não é necessário validar o tipo de titular ou valor nesta aula.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A23-01 | Conta("Ana") começa com titular Ana e saldo 0; Conta("Bia", 500) começa com 500. |
| A23-02 | Saldo inicial -1 → ValueError: saldo inválido. |
| A23-03 | Saldo 100, depositar 50 → 150; sacar 70 → 80; sacar 80 → 0. |
| A23-04 | Depósito e saque de 0 ou -1 → ValueError: valor deve ser positivo; saldo 100 preservado. |
| A23-05 | Sacar 101 de saldo 100 → ValueError: saldo insuficiente, sem alterar. |
| A23-06 | Depositar 50 na primeira de duas contas zeradas não modifica a segunda. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 23
```

```powershell
# Windows
py -3 estudar.py testar 23
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula23_classes -v` (Windows: `py -3 -m unittest testes.test_aula23_classes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A23-NN nesta tabela e [o código do teste](../../testes/test_aula23_classes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] O estado pertence à instância e não é compartilhado entre contas.
- [ ] Valido antes de modificar o saldo.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

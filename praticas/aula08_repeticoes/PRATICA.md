# Prática 08 — Repetições, contadores e acumuladores

**Objetivo:** Construir acumulações e contagens com limites corretos.

Leia primeiro o [conceito](../../estudos/01_fundamentos/aula08_repeticoes/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`somar_ate(limite)`: recebe inteiro não negativo; retorna int com a soma de 1 até limite, inclusive. Para 0, retorna 0.

`contar_pares(inicio, fim)`: recebe inteiros; retorna quantos pares existem no intervalo fechado de inicio até fim. Inclui negativos e zero. Se inicio for maior que fim, retorna 0. Use laços nesta prática; o uso do conceito é conferido por você no checklist, não por inspeção automática da sintaxe.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A08-01 | somar_ate(0) → 0; somar_ate(1) → 1. |
| A08-02 | somar_ate(5) → 15; somar_ate(100) → 5050. |
| A08-03 | contar_pares(1, 6) → 3. |
| A08-04 | contar_pares(-3, 2) → 3, contando -2, 0 e 2. |
| A08-05 | contar_pares(4, 4) → 1; (3, 3) → 0; (5, 2) → 0. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 08
```

```powershell
# Windows
py -3 estudar.py testar 08
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula08_repeticoes -v` (Windows: `py -3 -m unittest testes.test_aula08_repeticoes -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A08-NN nesta tabela e [o código do teste](../../testes/test_aula08_repeticoes.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Usei laços e sei explicar o valor inicial do acumulador.
- [ ] Sei por que o fim de range não faz parte da repetição.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

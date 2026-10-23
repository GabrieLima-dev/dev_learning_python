# Prática 27 — Escrita de testes e investigação de falhas

**Objetivo:** Corrigir um limite e escrever testes que detectam regressões reais.

Leia primeiro o [conceito](../../estudos/05_aplicacoes/aula27_testes_debugging/CONCEITO.md). Edite [pratica.py](pratica.py) e [test_pratica.py](test_pratica.py).

## Contrato da atividade

A função `frete(total_centavos)` já foi escrita, mas contém um erro de fronteira. A regra correta: inteiro negativo levanta `ValueError("total inválido")`; de 0 a 19999 retorna int 1200; a partir de 20000 retorna int 0. Corrija a função.

Implemente a classe `TestFrete` em `test_pratica.py`, com pelo menos quatro métodos test_ (pode usar os quatro esqueletos). Importe o módulo conforme fornecido. Seus testes devem passar para a função corrigida e falhar para cada mutação: **sempre zero**, **sempre 1200**, **gratuito somente acima de 20000**, **valor negativo retorna 1200 em vez de levantar erro**. Uma falha por exceção inesperada também detecta a mutação; o importante é que a suíte não a aceite. Use entradas e resultados explícitos, sem ler o código da função ou o teste avaliador.

Você pode executar somente seus testes com `python3 -m unittest praticas.aula27_testes_debugging.test_pratica -v` (Windows: `py -3 -m unittest ...`). O comando normal da aula executa também a avaliação de regressões. Esta é a única aula em que você deve editar um arquivo chamado test_: ele está dentro de praticas e é seu trabalho.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A27-01 | Função corrigida: -1 gera ValueError exato; 0 e 19999 → 1200; 20000 e 30000 → 0. |
| A27-02 | Sua classe TestFrete possui pelo menos quatro testes e todos passam na função corrigida. |
| A27-03 | Seus testes rejeitam quatro funções defeituosas públicas: sempre 0, sempre 1200, limite >20000 e negativo aceito. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 27
```

```powershell
# Windows
py -3 estudar.py testar 27
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula27_testes_debugging -v` (Windows: `py -3 -m unittest testes.test_aula27_testes_debugging -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A27-NN nesta tabela e [o código do teste](../../testes/test_aula27_testes_debugging.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Observei um teste falhar antes de corrigir a função.
- [ ] Meus testes têm resultados esperados explícitos e detectam as quatro regressões.
- [ ] Consigo explicar a causa do erro, além de apontar a linha alterada.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

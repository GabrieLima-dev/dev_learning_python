# Prática 25 — Herança e polimorfismo

**Objetivo:** Implementar uma hierarquia pequena e consumir objetos pela operação que oferecem.

Leia primeiro o [conceito](../../estudos/04_modelagem/aula25_polimorfismo/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`Forma.area()` levanta NotImplementedError, sem mensagem obrigatória. `Retangulo(Forma)` recebe largura e altura numéricas não negativas, armazena-as e devolve seu produto em `area()`. `Quadrado(Retangulo)` recebe lado e reaproveita Retangulo para representar duas dimensões iguais. A relação de herança é verificada.

`total_areas(formas)` recebe qualquer iterável de objetos com método area. Soma os retornos sem exigir que sejam instâncias de Forma. Entrada vazia retorna 0. Um objeto de teste que só possui area também precisa funcionar. Para os totais, int e float numericamente equivalentes são aceitos nesta aula. Não há dimensão inválida nos testes.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A25-01 | Forma().area() levanta NotImplementedError. |
| A25-02 | Retangulo(3, 4).area() → 12 e Retangulo(0, 5) → 0; herda de Forma. |
| A25-03 | Quadrado(2.5).area() → 6.25 e é Retangulo. |
| A25-04 | Total de Retangulo(3, 4) e Quadrado(2) → 16; vazio → 0. |
| A25-05 | Um iterador de objetos externos que oferecem area() retornando 7 → total 14. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 25
```

```powershell
# Windows
py -3 estudar.py testar 25
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula25_polimorfismo -v` (Windows: `py -3 -m unittest testes.test_aula25_polimorfismo -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A25-NN nesta tabela e [o código do teste](../../testes/test_aula25_polimorfismo.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Sei explicar a diferença entre possuir um objeto e especializar uma classe.
- [ ] total_areas aceita uma nova forma sem precisar conhecer o tipo dela.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

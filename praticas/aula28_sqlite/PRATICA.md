# Prática 28 — SQL e persistência com SQLite

**Objetivo:** Criar uma tabela, inserir com parâmetros e ler dados persistidos.

Leia primeiro o [conceito](../../estudos/05_aplicacoes/aula28_sqlite/CONCEITO.md). Edite [pratica.py](pratica.py).

## Contrato da atividade

`criar_tabela(conexao)`: cria, se não existir, `tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL)`, confirma a operação e retorna None. Repetir a chamada preserva linhas existentes.

`adicionar_tarefa(conexao, titulo)`: titulo é string. Remova espaços nas extremidades; se vazio, levante `ValueError("título vazio")`. Insira usando parâmetros SQL, confirme com commit e retorne o novo id como int positivo. Não feche a conexão. IDs crescem com as inclusões.

`listar_tarefas(conexao)`: retorna lista de tuplas `(id, titulo)`, ordenada por id crescente. Vazio retorna []. A tabela já existe. Títulos podem conter apóstrofos e texto parecido com SQL, que deve permanecer dado literal. Não é exigida uma inspeção da instrução escrita: o teste confirma o efeito e o checklist confere o uso de parâmetros.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A28-01 | Tabela recém-criada lista []; inserir " Estudar " retorna id 1 e lista [(1, "Estudar")]. |
| A28-02 | Duas inclusões obtêm IDs 1 e 2; chamar criar_tabela de novo preserva ambas na ordem. |
| A28-03 | Título com apóstrofo e SQL aparente é armazenado literalmente e a tabela continua existindo. |
| A28-04 | Títulos "" e "   " → ValueError: título vazio; não inserem linhas. |
| A28-05 | Inclusão em arquivo é visível por uma segunda conexão após fechar a primeira. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 28
```

```powershell
# Windows
py -3 estudar.py testar 28
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula28_sqlite -v` (Windows: `py -3 -m unittest testes.test_aula28_sqlite -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A28-NN nesta tabela e [o código do teste](../../testes/test_aula28_sqlite.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Passei dados separadamente do SQL, usando parâmetros.
- [ ] Confirmei as gravações e deixei o fechamento da conexão para quem a criou.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

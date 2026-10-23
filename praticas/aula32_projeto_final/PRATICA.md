# Prática 32 — Projeto final: gerenciador de tarefas

**Objetivo:** Entregar uma aplicação de tarefas persistente, testada e documentada, executável sem IA.

Leia primeiro o [conceito](../../estudos/06_projeto_final/aula32_projeto_final/CONCEITO.md). Edite [pratica.py](pratica.py) e [repositorio.py](repositorio.py).

## Contrato da atividade

Implemente `RepositorioTarefas(caminho)` em `repositorio.py`. O caminho é str ou Path de um banco SQLite em diretório existente. O construtor prepara o banco sem apagar dados. O esquema é de sua escolha, mas deve usar SQLite de verdade e IDs inteiros positivos crescentes iniciando em 1 em banco vazio.

- `adicionar(titulo)`: titulo é string; remova espaços nas extremidades. Comprimento após strip deve ser de 1 a 80 caracteres. Inválido levanta `ValueError("título inválido")` sem inserir. Válido retorna id int e começa pendente. Duplicatas de título são permitidas. Use parâmetros SQL.
- `listar(pendentes=False)`: retorna lista de dicts com exatamente `id` int, `titulo` str e `concluida` bool, por id crescente. Quando pendentes=True, retorna só tarefas não concluídas. Vazio retorna [].
- `concluir(identificador)`: recebe int. Se existe, marca como concluída, persiste e retorna True, mesmo se já estava concluída. Se não existe, retorna False sem alterar outras tarefas.

Implemente `main(argv=None)` em `pratica.py` com argparse. Opção global `--banco CAMINHO` tem padrão `tarefas.sqlite3` e deve vir **antes** do subcomando. Os subcomandos são:

| Comando | Resultado em sucesso |
|---|---|
| `adicionar "Título"` | stdout `Criada: ID` + quebra de linha; retorna 0 |
| `listar` | uma linha por tarefa: `ID | [ ] | Título` se pendente ou `ID | [x] | Título` se concluída; retorna 0 |
| `listar --pendentes` | mesmo formato, somente pendentes; retorna 0 |
| `concluir ID` | stdout `Concluída: ID` + quebra; retorna 0 se a tarefa existe |

Lista vazia imprime `Nenhuma tarefa.` + quebra de linha. Título inválido imprime somente `Erro: título inválido.` + quebra em stderr, deixa stdout vazio e retorna 1. ID inexistente imprime somente `Erro: tarefa não encontrada.` + quebra em stderr e retorna 1. Concluir uma tarefa já concluída continua sendo sucesso. Comando ausente, desconhecido ou ID não inteiro usa o erro padrão do argparse (SystemExit 2). `--help` funciona sem criar o banco. Não use input. O bloco de execução já está pronto.

Execute depois de implementar: `python3 -m praticas.aula32_projeto_final.pratica --banco rascunho.sqlite3 adicionar "Estudar Python"`, seguido de `listar`, `concluir 1` e `listar --pendentes` com o mesmo --banco. No Windows troque python3 por py -3. Complete também `README_PROJETO.md` com sua explicação e os comandos reais. Esse documento e a prática Git são autoavaliações, sem correção automática de conteúdo.

## Casos públicos: o que será aceito

Cada linha corresponde a um método do teste. Todos os casos de avaliação estão neste repositório; não há servidor nem testes ocultos. Além dos exemplos, implemente a regra para qualquer entrada dentro do domínio descrito.

| Caso | Entrada, resultado esperado e observações |
|---|---|
| A32-01 | Banco vazio lista []; adicionar " Estudar " e "Estudar" gera IDs 1 e 2, pendentes, com títulos normalizados. |
| A32-02 | Título de 80 caracteres aceito; vazio, espaços e 81 caracteres rejeitados sem inserir. |
| A32-03 | Concluir id 1 duas vezes retorna True; id 99 retorna False; listar pendentes mostra só id 2. |
| A32-04 | Outra instância recupera título com apóstrofo e situação concluída; arquivo possui cabeçalho SQLite. |
| A32-05 | CLI: adicionar, listar, concluir e listar --pendentes produzem as mensagens exatas e códigos 0. |
| A32-06 | CLI título vazio e ID inexistente: código 1, stdout vazio, stderr com mensagem exata. |
| A32-07 | CLI comando ausente, desconhecido ou ID não inteiro: SystemExit 2; --help: SystemExit 0 sem criar banco. |
| A32-08 | Execuções reais em processos distintos: adicionar "Persistência" e listar recupera id 1 pendente. |

## Regras de implementação

Mantenha os nomes e parâmetros fornecidos. Substitua os TODOs e as exceções provisórias nas partes a implementar. Não altere os testes de avaliação para obter aprovação. Não leia os testes a partir da sua implementação nem devolva respostas fixas só para os exemplos. Só use input, print, rede ou arquivos quando o contrato pedir.

Salvo exceção explícita no contrato, o teste confere o tipo do retorno além do valor: `True` não substitui `1`, uma tupla não substitui uma lista, e texto numérico não substitui número. Para floats há tolerância absoluta/relativa de 1e-9. Campos internos de listas, tuplas e dicts também têm tipos conferidos.

## Executar e interpretar

Na raiz do projeto, use:

```bash
# macOS ou Linux
python3 estudar.py testar 32
```

```powershell
# Windows
py -3 estudar.py testar 32
```

Para chamar diretamente o unittest, use `python3 -m unittest testes.test_aula32_projeto_final -v` (Windows: `py -3 -m unittest testes.test_aula32_projeto_final -v`). O comando direto não tem o limite de duração do comando da trilha e não registra progresso.

`OK` indica que os casos executados passaram. No arquivo inicial, falhas são esperadas. Consulte os nomes A32-NN nesta tabela e [o código do teste](../../testes/test_aula32_projeto_final.py). Use [o guia de leitura](../../docs/COMO_LER_TESTES.md) para distinguir erro de sintaxe, retorno errado e implementação pendente.

## Autoavaliação antes da conclusão

- [ ] Completei README_PROJETO.md e fiz a demonstração com banco de rascunho.
- [ ] Separei interface e persistência; uso parâmetros SQL e fecho conexões.
- [ ] Revisei git status, git diff e o histórico, sem incluir bancos, credenciais ou progresso pessoal.
- [ ] Se publico minha cópia, conferi o remoto e sincronizei a branch principal com meu GitHub.

Quando esta for sua aula atual e todos os itens estiverem conferidos, execute `python3 estudar.py concluir --revisei` (Windows: `py -3 estudar.py concluir --revisei`). O comando executa os testes novamente e só registra a conclusão em caso de sucesso. A partir da aula 02, revise `git status`, `git diff` e registre um commit pequeno na sua própria cópia.

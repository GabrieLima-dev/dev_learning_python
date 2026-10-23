# 32 — Projeto final: gerenciador de tarefas

**Objetivo:** Entregar uma aplicação de tarefas persistente, testada e documentada, executável sem IA.

O projeto final reúne persistência, classes, validação, testes e interface de terminal. Você construirá um gerenciador de tarefas que continua com os dados disponíveis depois de encerrar o processo. O programa permitirá adicionar, listar e concluir tarefas.

Separe a persistência da interface. RepositorioTarefas representa as operações sobre os dados; main interpreta argumentos e apresenta resultados. Assim, um teste pode verificar as regras sem abrir um terminal, enquanto outro executa o programa completo para confirmar que as partes estão conectadas.

Uma tarefa tem identidade, título e situação. O identificador é gerado pelo banco e não depende da posição numa lista. Concluir uma tarefa duas vezes deve manter o mesmo estado: essa propriedade é chamada de idempotência. Uma tarefa inexistente é um resultado diferente de uma tarefa já concluída.

Use um caminho de banco recebido de fora. Os testes precisam de bancos temporários, e o usuário pode escolher onde guardar seus dados. Sempre confirme transações e feche conexões criadas por sua implementação. Uma forma simples é abrir uma conexão por operação, confirmar alterações e garantir seu fechamento; outra é administrar explicitamente o ciclo de vida, desde que a interface definida seja atendida.

Erros de argumento pertencem ao parser. Erros de domínio, como título vazio, precisam de uma mensagem simples e código de saída 1. Não capture qualquer exceção para escondê-la: falhas inesperadas devem continuar visíveis durante o desenvolvimento.

Antes de considerar o projeto pronto, faça uma demonstração manual em um banco de rascunho, escreva as instruções no README do projeto e revise o histórico Git. Os testes automáticos confirmam o contrato abaixo e a persistência entre processos. A qualidade da explicação e a organização do histórico continuam sendo responsabilidades de autoavaliação.

## Exemplo comentado

```python
# Exemplo de separação de responsabilidade, sem implementar o projeto:
class Catalogo:
    def listar_nomes(self):
        return ["Exemplo"]

# A interface usa o resultado do domínio para apresentar texto.
for nome in Catalogo().listar_nomes():
    print(nome)
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.


## Recursos para conectar as partes

Você já usou SELECT e INSERT. Para mudar registros existentes, SQL usa `UPDATE tabela SET campo = ? WHERE id = ?`, passando os valores separados da instrução. Sem WHERE, todas as linhas poderiam ser modificadas. `cursor.rowcount` indica quantas linhas a operação atingiu e ajuda a distinguir um identificador existente de um inexistente. Confirme com commit para outra conexão enxergar a alteração.

SQLite pode guardar a situação booleana como inteiro 0 ou 1. Na fronteira de saída da aplicação, `bool(0)` é False e `bool(1)` é True. Retorne o tipo booleano pedido no contrato. Um SELECT com WHERE restringe quais linhas são devolvidas, enquanto ORDER BY define a ordem; os dois podem ser usados na mesma consulta.

O exemplo abaixo mostra atualização em outro domínio. O contexto `closing` garante o fechamento da conexão. Usar somente `with sqlite3.connect(...)` gerencia transações, mas não substitui o fechamento da conexão.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as conexao:
    conexao.execute("CREATE TABLE luzes (id INTEGER PRIMARY KEY, ligada INTEGER)")
    conexao.execute("INSERT INTO luzes VALUES (?, ?)", (1, 0))
    cursor = conexao.execute("UPDATE luzes SET ligada = ? WHERE id = ?", (1, 1))
    conexao.commit()
    print(cursor.rowcount)  # 1 linha atingida
    linha = conexao.execute("SELECT ligada FROM luzes WHERE id = ?", (1,)).fetchone()
    print(bool(linha[0]))  # True
```

No argparse, subcomandos têm seus próprios argumentos. `add_subparsers(dest="acao", required=True)` registra onde guardar o nome escolhido e torna a escolha obrigatória. Cada `add_parser` cria a configuração de um subcomando. Opções globais são declaradas no parser principal e aparecem antes do subcomando; opções específicas são declaradas no parser correspondente.

```python
import argparse

parser = argparse.ArgumentParser(description="Exemplo de subcomando")
parser.add_argument("--prefixo", default="Texto")
subcomandos = parser.add_subparsers(dest="acao", required=True)
mostrar = subcomandos.add_parser("mostrar")
mostrar.add_argument("palavra")
mostrar.add_argument("--maiusculas", action="store_true")
args = parser.parse_args(["--prefixo", "Mensagem", "mostrar", "olá", "--maiusculas"])
print(args.acao)       # mostrar
print(args.palavra)    # olá
print(args.maiusculas) # True
```

`action="store_true"` cria uma opção booleana: ela vale False quando ausente e True quando presente. Para escrever erros de domínio em stderr, use `print(mensagem, file=sys.stderr)` após importar sys. Deixe os erros de uso do comando para o próprio argparse. A ajuda deve ser interpretada antes de criar o repositório, para não abrir um banco ao pedir somente instruções.

## Antes de seguir

- [ ] Completei README_PROJETO.md e fiz a demonstração com banco de rascunho.
- [ ] Separei interface e persistência; uso parâmetros SQL e fecho conexões.
- [ ] Revisei git status, git diff e o histórico, sem incluir bancos, credenciais ou progresso pessoal.
- [ ] Se publico minha cópia, conferi o remoto e sincronizei a branch principal com meu GitHub.

Abra o [enunciado](../../../praticas/aula32_projeto_final/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula32_projeto_final/pratica.py) e consulte o [teste público](../../../testes/test_aula32_projeto_final.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 32
```

```powershell
# Windows
py -3 estudar.py testar 32
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

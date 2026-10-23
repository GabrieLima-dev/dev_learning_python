# 28 — SQL e persistência com SQLite

**Objetivo:** Criar uma tabela, inserir com parâmetros e ler dados persistidos.

Um banco relacional organiza dados em tabelas. Uma linha representa um registro, e colunas representam campos. SQL é a linguagem usada para definir estruturas e consultar ou alterar dados. SQLite guarda um banco em arquivo e pode ser usado pelo módulo sqlite3 da biblioteca padrão.

Uma conexão representa o acesso ao banco. `execute` devolve um cursor, que contém informações sobre a operação. Depois de um INSERT, `cursor.lastrowid` informa o identificador gerado. Em uma consulta, `cursor.fetchall()` devolve uma lista de tuplas, uma por linha, com os campos na ordem do SELECT. `execute` envia uma instrução SQL. `CREATE TABLE IF NOT EXISTS` permite preparar a tabela sem apagar os dados de uma execução anterior. `INSERT` acrescenta uma linha, e `SELECT ... ORDER BY ...` define explicitamente a ordem da consulta.

Use parâmetros para valores SQL. Em vez de montar SQL concatenando o título digitado, escreva placeholders `?` e entregue uma tupla de valores separadamente. Além de evitar problemas com aspas, isso impede que o valor seja interpretado como parte do comando SQL. A instrução e os dados têm papéis diferentes.

Uma transação agrupa alterações. Commit confirma a gravação e rollback desfaz alterações ainda não confirmadas. Nesta prática cada inclusão deve confirmar sua própria gravação. A conexão recebida continua pertencendo a quem chamou; não a feche dentro dessas funções.

Os testes usam tanto um banco em memória quanto um arquivo temporário reaberto por outra conexão. Um teste apenas na mesma conexão poderia enxergar uma linha ainda não confirmada e dar uma impressão incorreta de persistência.

Não é necessário instalar servidor SQL. O comando ambiente verifica se o Python da máquina inclui sqlite3, e o README explica como verificar a instalação.

## Exemplo comentado

```python
import sqlite3

conexao = sqlite3.connect(":memory:")
conexao.execute("CREATE TABLE cores (nome TEXT NOT NULL)")
conexao.execute("INSERT INTO cores(nome) VALUES (?)", ("azul",))
conexao.commit()
print(conexao.execute("SELECT nome FROM cores").fetchall())
conexao.close()
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Passei dados separadamente do SQL, usando parâmetros.
- [ ] Confirmei as gravações e deixei o fechamento da conexão para quem a criou.

Abra o [enunciado](../../../praticas/aula28_sqlite/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula28_sqlite/pratica.py) e consulte o [teste público](../../../testes/test_aula28_sqlite.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 28
```

```powershell
# Windows
py -3 estudar.py testar 28
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

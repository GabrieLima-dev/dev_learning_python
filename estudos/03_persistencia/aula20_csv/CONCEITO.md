# 20 — CSV e intercâmbio de tabelas

**Objetivo:** Exportar e importar produtos sem quebrar campos com vírgulas ou aspas.

CSV representa tabelas em arquivos de texto. Cada linha é um registro e os campos são separados por um delimitador. Um cabeçalho pode informar os nomes das colunas. Apesar do nome, nem todo arquivo usa vírgula; o contrato precisa dizer qual dialeto esperar.

Dividir a linha com split não é suficiente para ler CSV corretamente. Um nome de produto pode conter vírgula, aspas ou até quebra de linha. O módulo csv cuida das regras de escape e aspas para esses casos. DictReader associa cada coluna ao nome do cabeçalho e DictWriter escreve registros a partir de dicionários.

Ao abrir arquivos para o módulo csv, use `newline=""` e `encoding="utf-8"`. Isso permite que o próprio módulo gerencie as quebras de linha de forma consistente, inclusive no Windows. O padrão de saída pode usar CRLF; nesta atividade os testes comparam registros, não exigem bytes de quebra específicos.

CSV não carrega informações de tipo como um objeto Python. O texto `"1200"` lido de uma célula precisa ser convertido para int se representa centavos. O cabeçalho e a ordem das colunas também são parte do contrato do arquivo, embora a ordem interna das chaves de um dict não seja o objetivo da aula.

A prática usa dados válidos e arquivos existentes na leitura. O foco é ida e volta com preservação dos valores, incluindo caracteres que exigem escape. Não há obrigação de tratar arquivos malformados nesta aula.

## Exemplo comentado

```python
import csv
import io

texto = 'cidade,populacao\n"Rio, exemplo",10\n'
for linha in csv.DictReader(io.StringIO(texto)):
    print(linha["cidade"], int(linha["populacao"]))
```


Para escrever registros com DictWriter, informe `fieldnames` na ordem das colunas. `writeheader()` grava os nomes; `writerow(registro)` grava um registro e `writerows(registros)` grava vários. Este exemplo usa um arquivo de texto em memória apenas para mostrar a API:

```python
import csv
import io

saida = io.StringIO(newline="")
escritor = csv.DictWriter(saida, fieldnames=["cidade", "habitantes"])
escritor.writeheader()
escritor.writerow({"cidade": "Cidade, exemplo", "habitantes": 10})
print(saida.getvalue())
```

Ao usar um arquivo real, passe o arquivo aberto no lugar de saida. A escrita do cabeçalho precisa acontecer mesmo se não houver nenhum registro.

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Usei o módulo csv para lidar com campos especiais.
- [ ] Abri os arquivos com UTF-8 e newline apropriado.

Abra o [enunciado](../../../praticas/aula20_csv/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula20_csv/pratica.py) e consulte o [teste público](../../../testes/test_aula20_csv.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 20
```

```powershell
# Windows
py -3 estudar.py testar 20
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

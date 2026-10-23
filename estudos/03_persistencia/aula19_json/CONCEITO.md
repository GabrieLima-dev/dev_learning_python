# 19 — JSON e dados estruturados

**Objetivo:** Persistir configurações e distinguir ausência, sintaxe inválida e formato inválido.

JSON é um formato de texto para representar dados estruturados. Ele possui objetos, listas, strings, números, booleanos e null. Em Python, esses dados correspondem geralmente a dict, list, str, int ou float, bool e None. Um arquivo JSON continua sendo texto; não é um objeto Python até ser interpretado.

O módulo json realiza a conversão. `json.dumps(dados)` produz uma string JSON; `json.loads(texto)` interpreta uma string. `json.dump` e `json.load` trabalham com arquivos abertos. A opção ensure_ascii=False mantém caracteres acentuados legíveis na representação, e indent facilita a leitura humana.

Não use eval para ler JSON. JSON não é código Python e o leitor apropriado valida sua sintaxe sem executar instruções. Texto malformado levanta JSONDecodeError. Para verificar um tipo de dado, `isinstance(valor, dict)` devolve True quando valor é um dicionário; a mesma função pode conferir list ou str. Além da sintaxe, a aplicação pode exigir um formato de dados: uma lista é JSON válido, mas não serve quando o contrato espera um dicionário de configurações.

Ausência de arquivo e conteúdo corrompido têm significados diferentes. A ausência pode representar uma aplicação ainda sem configuração. Uma configuração ilegível merece um erro visível; apagá-la silenciosamente esconderia informação que poderia ser recuperada.

Os testes vão ler o arquivo salvo e comparar os dados, sem exigir uma indentação específica ou ordem de chaves. Assim, você tem liberdade para escolher uma apresentação legível sem perder interoperabilidade. O domínio de entrada desta prática contém somente valores aceitos pelo JSON.

## Exemplo comentado

```python
import json

texto = json.dumps({"cidade": "Maceió", "ativo": True}, ensure_ascii=False)
print(texto)
dados = json.loads(texto)
print(dados["ativo"])  # True
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Uso json em vez de avaliar o texto como código.
- [ ] Diferencio arquivo ausente, JSON malformado e JSON com tipo inadequado.

Abra o [enunciado](../../../praticas/aula19_json/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula19_json/pratica.py) e consulte o [teste público](../../../testes/test_aula19_json.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 19
```

```powershell
# Windows
py -3 estudar.py testar 19
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

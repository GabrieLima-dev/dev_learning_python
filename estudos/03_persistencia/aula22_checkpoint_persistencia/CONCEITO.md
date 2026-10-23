# 22 — Checkpoint: diário de eventos em JSON

**Objetivo:** Registrar eventos acumulativos com validação e preservação do arquivo em erros previstos.

Este checkpoint transforma arquivos e estruturas de dados em um pequeno registro persistente. Cada evento é um dicionário simples; o arquivo guarda uma lista de eventos na ordem em que foram registrados. Executar o programa outra vez deve recuperar os eventos anteriores.

Uma operação de acrescentar envolve ler o estado atual, validar a nova entrada, produzir o novo estado e gravá-lo. A ordem dessas responsabilidades importa. Se o novo evento é inválido, o arquivo anterior deve permanecer intacto. Se o arquivo está corrompido, não o substitua por uma lista vazia silenciosamente.

Ausência de arquivo representa um diário ainda sem eventos. Uma lista JSON vazia representa um diário existente sem eventos. Ambos retornam uma lista vazia na leitura, mas somente o registro de um evento precisa criar um arquivo novo.

Não é necessário implementar acesso simultâneo, bloqueio ou recuperação após falta de energia nesta prática. Essas situações exigem contratos adicionais. Aqui garantimos a preservação diante dos erros de validação descritos e o fechamento normal dos arquivos. Essa delimitação permite testar o comportamento com precisão.

Os testes usam arquivos novos em diretórios temporários e também arquivos escritos pelo próprio teste. Isso evita uma falsa segurança em que salvar e ler cometem erros compatíveis entre si. Compare sempre o conteúdo persistido com o formato público JSON.

Ao concluir, explique o que acontece em quatro situações: primeiro registro, segundo registro, evento inválido e arquivo corrompido. Se cada caminho estiver claro, você terá uma boa base para usar um banco de dados adiante.

## Exemplo comentado

```python
import json

historico = [{"tipo": "abertura", "descricao": "Início do turno"}]
texto = json.dumps(historico, ensure_ascii=False)
print(json.loads(texto)[0]["tipo"])
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo explicar os caminhos de primeira escrita, acréscimo e falha.
- [ ] Nenhum erro previsto destrói um histórico anterior.
- [ ] Revisei meu commit e sincronizei minha cópia no GitHub, se configurada.

Abra o [enunciado](../../../praticas/aula22_checkpoint_persistencia/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula22_checkpoint_persistencia/pratica.py) e consulte o [teste público](../../../testes/test_aula22_checkpoint_persistencia.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 22
```

```powershell
# Windows
py -3 estudar.py testar 22
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

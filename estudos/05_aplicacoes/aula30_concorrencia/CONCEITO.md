# 30 — Concorrência com tarefas independentes

**Objetivo:** Executar tarefas independentes simultaneamente, preservando ordem e propagando falhas.

Concorrência permite que várias tarefas avancem no mesmo intervalo de tempo. Threads compartilham a memória do processo e são úteis principalmente quando as tarefas passam tempo esperando, como em operações de entrada e saída. Criar threads não torna automaticamente qualquer cálculo mais rápido.

ThreadPoolExecutor administra um conjunto de trabalhadores. O bloco with cuida do encerramento. Seu método map aplica uma função a vários itens e disponibiliza os resultados na ordem das entradas, mesmo quando as tarefas terminam em outra ordem. A chamada a list consome os resultados e pode propagar uma exceção de uma tarefa.

Passar uma função como argumento é uma forma de separar o que deve ser feito de como as tarefas serão organizadas. Por exemplo, uma função pode transformar um número enquanto outra decide executá-la em vários trabalhadores. Essa separação também torna o exercício testável sem conexão externa.

Dados compartilhados que são modificados por várias threads exigem coordenação. Esta prática evita esse problema: a função recebida é segura para execução concorrente e cada resultado pertence a uma entrada. Não crie variáveis globais para acumular respostas.

Um teste de concorrência não deveria depender apenas de medir se uma execução foi rápida. A avaliação desta aula usa uma barreira: duas tarefas precisam chegar ao mesmo ponto para continuar. Se você executar uma após a outra, a primeira não verá a segunda e o teste falhará por tempo limite. A barreira tem limite de cinco segundos para encerrar de forma previsível.

## Exemplo comentado

```python
from concurrent.futures import ThreadPoolExecutor

def tamanho(texto):
    return len(texto)

with ThreadPoolExecutor(max_workers=2) as executor:
    resultados = list(executor.map(tamanho, ["sol", "chuva"]))
print(resultados)  # [3, 5]
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Consigo explicar por que as tarefas da prática podem ser independentes.
- [ ] A ordem do resultado acompanha a entrada e falhas não são ocultadas.

Abra o [enunciado](../../../praticas/aula30_concorrencia/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula30_concorrencia/pratica.py) e consulte o [teste público](../../../testes/test_aula30_concorrencia.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 30
```

```powershell
# Windows
py -3 estudar.py testar 30
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

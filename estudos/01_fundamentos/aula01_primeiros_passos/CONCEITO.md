# 01 — Primeiros passos e leitura de testes

**Objetivo:** Escrever sua primeira função e reconhecer uma execução de teste bem-sucedida.

Python executa instruções escritas em arquivos com a extensão `.py`. O terminal é o lugar em que você pede ao computador para executar um arquivo. O editor é onde você altera esse arquivo. Salvar uma edição no editor e executar o programa são ações diferentes: se não salvar, o Python continuará lendo a versão anterior.

Uma string é um texto entre aspas. `print()` mostra um valor na tela. Já `return` entrega um valor para quem chamou uma função. Essa diferença aparece desde a primeira prática: os testes chamam sua função e comparam o valor devolvido, sem procurar uma mensagem no terminal.

Uma função é um bloco com nome. A linha `def nome():` apresenta o bloco; as linhas abaixo ficam recuadas com quatro espaços. Os parênteses permitem receber dados, mas nesta aula ficam vazios. Não é necessário dominar funções agora: mantenha a estrutura fornecida e escreva a devolução dentro dela. A aula de funções aprofundará parâmetros, valores padrão e composição.

Um teste é outro programa que faz uma chamada e compara o resultado real com um resultado esperado. `assertEqual(real, esperado)` verifica igualdade. `FAIL` indica uma comparação que não passou. `ERROR` indica uma interrupção, como uma função ainda não implementada. `OK` significa que todos os casos executados passaram. A palavra `NotImplementedError` nos arquivos iniciais é um lembrete proposital: substitua essa linha pela sua implementação.

Comece abrindo o arquivo de prática, identifique a função e execute os testes antes de editar. Ver a falha inicial faz parte da aula. Depois altere, salve e execute novamente. O teste não edita seu código.

## Exemplo comentado

```python
def mensagem_do_dia():
    return "Hoje vou praticar."

texto = mensagem_do_dia()
print(texto)  # mostra Hoje vou praticar.
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Sei distinguir o editor do terminal.
- [ ] Consigo explicar por que return e print produzem resultados diferentes.
- [ ] Executei os testes antes e depois de implementar.

Abra o [enunciado](../../../praticas/aula01_primeiros_passos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula01_primeiros_passos/pratica.py) e consulte o [teste público](../../../testes/test_aula01_primeiros_passos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 01
```

```powershell
# Windows
py -3 estudar.py testar 01
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

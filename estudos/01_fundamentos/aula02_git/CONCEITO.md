# 02 — Git e registro da evolução

**Objetivo:** Reconhecer os comandos de inspeção e começar a registrar sua evolução.

Git guarda versões de arquivos. Um repositório é uma pasta acompanhada por esse histórico. O clone baixa uma cópia do repositório; o commit registra uma versão local; o push envia commits a um remoto em que você tenha permissão. GitHub é um serviço para hospedar repositórios, e não é necessário para executar Python.

O fluxo básico começa em `git status`, que lista arquivos novos e alterados. `git diff` mostra as alterações ainda não preparadas. `git add caminho/do/arquivo` prepara um arquivo para o próximo commit. `git diff --staged` permite conferir a seleção. Por último, `git commit -m "mensagem"` registra a mudança. A mensagem descreve uma unidade de trabalho, por exemplo, concluir uma prática.

O arquivo `.gitignore` lista arquivos locais que normalmente não devem ir para o histórico. Neste projeto, `.learning/` contém o progresso pessoal e `__pycache__/` contém arquivos gerados pelo Python. Eles são dispensáveis para os colegas. Ignorar um arquivo não remove um segredo que já tenha sido enviado: por isso revise o diff antes de registrar.

Para a parte automática desta aula, você preencherá constantes de texto. Uma constante usa um nome em maiúsculas por convenção; o Python não impede que ela mude. Isso nos permite verificar se você reconhece os comandos, sem executar Git ou modificar seu histórico por você. As ações reais ficam no roteiro manual abaixo. Testes verdes comprovam as respostas, não comprovam que um commit ou push aconteceu.

Na sua cópia, execute `git status` e `git diff`. Depois de resolver a aula, prepare apenas o arquivo editado, confira o diff preparado e crie um commit. Se clonou o repositório do professor e quer enviar sua evolução, crie sua própria cópia pelo template conforme o README antes de configurar o remoto.

## Exemplo comentado

```python
# Uma constante guarda uma informação conhecida.
EXTENSAO_PYTHON = ".py"
print(EXTENSAO_PYTHON)
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Executei status e diff e sei explicar a saída.
- [ ] Sei que commit é local e push envia para o remoto.
- [ ] Revisei os arquivos preparados e registrei uma mudança pequena na minha cópia.

Abra o [enunciado](../../../praticas/aula02_git/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula02_git/pratica.py) e consulte o [teste público](../../../testes/test_aula02_git.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 02
```

```powershell
# Windows
py -3 estudar.py testar 02
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

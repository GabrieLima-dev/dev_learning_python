# DEV_LEARNING_PYTHON

Aprenda Python no seu computador: leia a aula, resolva a prática, execute os testes e registre sua conclusão. **Todo o material já está neste repositório** Depois de instalar as ferramentas e clonar o projeto, as aulas e avaliações funcionam sem internet.

São **32 aulas, 3 checkpoints e 149 casos públicos de avaliação**, dos primeiros passos até um gerenciador de tarefas com SQLite. Cada prática informa quais dados recebe, o que deve devolver, quais erros são esperados e quais exemplos serão verificados. O código inicial tem TODOs para você resolver; falhas nas práticas ainda não implementadas são esperadas.

[Comece pelo índice das aulas](estudos/README.md) · [Como ler testes](docs/COMO_LER_TESTES.md) · [Guia do professor](docs/PROFESSOR.md) · [Referências](docs/REFERENCIAS.md)

## Como usar — passo a passo rápido

Se ainda não instalou o Python ou baixou o projeto, siga primeiro as seções **1. Instalar o necessário** e **2. Clonar sua cópia**, abaixo.

1. **Abra a pasta do projeto no editor e abra um terminal nessa pasta.** Você deve estar onde fica o arquivo `estudar.py`.
2. **Execute o comando de começar ou retomar**, indicado na tabela abaixo. Ele mostra os caminhos dos arquivos da sua aula atual.
3. **Leia e pratique.** Abra o `CONCEITO.md` para estudar, depois o `PRATICA.md` para entender a tarefa e os resultados esperados. Complete os TODOs no `pratica.py` e salve o arquivo.
4. **Execute o comando de testar.** Se aparecer uma falha, leia o caso indicado, corrija sua prática e teste novamente. Quando aparecer `OK`, confira o checklist no enunciado.
5. **Execute o comando de concluir.** Ele testa novamente e salva seu progresso se tudo passar. Depois, use o comando de retomar para encontrar a próxima aula.

| O que fazer | Windows — PowerShell | macOS ou Linux — Terminal |
|---|---|---|
| Começar ou retomar | `py -3 estudar.py continuar` | `python3 estudar.py continuar` |
| Testar a aula atual | `py -3 estudar.py testar` | `python3 estudar.py testar` |
| Concluir após conferir o checklist | `py -3 estudar.py concluir --revisei` | `python3 estudar.py concluir --revisei` |
| Consultar seu progresso | `py -3 estudar.py status` | `python3 estudar.py status` |

**Na próxima vez, basta abrir a pasta e executar `continuar`: o sistema lembra onde você parou.** Você lê os materiais no editor e usa o terminal para executar os comandos; não precisa pedir nada a uma IA.

## O que você vai aprender

| Etapa | Aulas | Conteúdo |
|---|---|---|
| Fundamentos | 01–10 | Ambiente, Git, tipos, conversões, contas, textos, entrada e saída, decisões, repetições, listas e relatório de notas. |
| Organização | 11–17 | Tuplas, conjuntos, dicionários, funções, compreensões, ordenação, exceções, módulos e resumo de vendas. |
| Persistência | 18–22 | Texto, caminhos, JSON, CSV, datas, Decimal e diário de eventos. |
| Modelagem | 23–26 | Classes, estado, dataclasses, composição, herança, polimorfismo e geradores. |
| Aplicações | 27–31 | Escrita de testes, debugging, SQLite, contratos HTTP sem rede, concorrência e linha de comando. |
| Projeto final | 32 | Gerenciador de tarefas com dados persistentes, comandos de terminal e documentação. |

A trilha cobre fundamentos e aplicações locais de Python. Frameworks web, ciência de dados, deploy e servidores externos ficam para trilhas posteriores. Nenhum desses componentes é necessário para concluir este projeto.

## 1. Instalar o necessário

Você precisa de **Python 3.11 ou superior**, **Git** para clonar/versionar e um editor de texto. Python 3.14 é uma opção para acompanhar esta edição. O IDLE que acompanha a instalação oficial também permite editar arquivos; você pode usar outro editor de sua preferência. Para ler Markdown, abra os arquivos no editor ou consulte-os no GitHub.

**Não é necessário instalar pytest, banco de dados separado, pacotes com pip ou uma ferramenta de IA.** Os testes usam unittest e o banco usa sqlite3, da biblioteca padrão. Verifique a disponibilidade na sua instalação pelo comando ambiente abaixo.

### Windows — PowerShell

1. Baixe e instale o **Python Install Manager** pelo [site oficial do Python](https://www.python.org/downloads/windows/).
2. Abra um novo PowerShell e instale o runtime:

   ```powershell
   py install 3.14
   py -3 --version
   ```

3. Instale Git pelo [instalador oficial indicado para Windows](https://git-scm.com/install/windows). Aceite a opção que disponibiliza Git no terminal.
4. Feche e abra o PowerShell, depois execute `git --version`.

Se já tem Python 3.11 ou superior e `py -3 --version` funciona, não precisa reinstalar. O comando `py install` pertence ao novo gerenciador; um launcher antigo pode não reconhecê-lo. Nesse caso, confira a versão já instalada ou instale o gerenciador oficial. [Instalação e solução de problemas do Python no Windows](https://docs.python.org/3/using/windows.html).

### macOS — Terminal

1. Baixe o instalador `.pkg` do Python na [página oficial para macOS](https://www.python.org/downloads/macos/).
2. Abra o arquivo e siga o instalador. Se ele oferecer `Install Certificates.command`, execute esse passo conforme as instruções da instalação.
3. No Terminal, execute `python3 --version` e confirme 3.11 ou superior. [Guia oficial do Python no macOS](https://docs.python.org/3/using/mac.html).
4. Execute `git --version`. Se Git estiver ausente, instale as ferramentas de linha de comando da Apple:

   ```bash
   xcode-select --install
   ```

   Conclua a janela de instalação e teste `git --version` novamente. Esse método está listado nas [opções oficiais de instalação do Git](https://git-scm.com/install/mac).

### Linux — Terminal

No Ubuntu ou Debian:

```bash
sudo apt update
sudo apt install python3 git
python3 --version
git --version
```

No Fedora:

```bash
sudo dnf install python3 git
python3 --version
git --version
```

Confirme Python **3.11 ou superior**. Se a distribuição fornece versão anterior, use uma versão atual da distribuição ou instale um Python compatível pelo procedimento dela; não substitua manualmente o Python utilizado pelo sistema. Outras distribuições têm gerenciadores próprios. Consulte as [opções de Git para Linux](https://git-scm.com/install/linux) e o [guia do Python em Unix](https://docs.python.org/3/using/unix.html).

### Ambiente virtual é opcional nesta trilha

Como não há pacotes externos, você pode usar diretamente os comandos acima. Se quiser praticar isolamento, consulte [ambientes virtuais](docs/AMBIENTE_VIRTUAL.md). Não envie `.venv/` aos colegas.

## 2. Clonar sua cópia

O professor deve enviar a URL do repositório publicado. **Substitua `COLE_AQUI_A_URL_HTTPS` abaixo por essa URL**, mantendo o nome de destino. Este exemplo não pressupõe que exista um endereço público específico:

```bash
git clone "COLE_AQUI_A_URL_HTTPS" dev_learning_python
cd dev_learning_python
```

Se quiser enviar sua evolução para seu próprio GitHub, crie antes uma cópia usando **Use this template**, quando disponível, ou um fork, e clone a URL dessa cópia. Um clone do repositório do professor normalmente não permite push para ele. O estudo local funciona mesmo sem configurar envio ao GitHub.

Abra a pasta `dev_learning_python` no editor. Todos os comandos seguintes devem ser executados na pasta onde está `estudar.py`.

## 3. Verificar a instalação

No macOS/Linux:

```bash
python3 estudar.py ambiente
python3 estudar.py verificar
python3 estudar.py continuar
```

No Windows:

```powershell
py -3 estudar.py ambiente
py -3 estudar.py verificar
py -3 estudar.py continuar
```

`ambiente` confere o interpretador e as bibliotecas. `verificar` valida os materiais e executa os testes do **sistema de estudos**, sem exigir exercícios resolvidos. Uma instalação íntegra termina com `Sistema pronto`. `continuar` indica o material da aula atual; no primeiro uso será a aula 01.

Se aparecer `NotImplementedError` ao usar **testar**, significa que a prática ainda precisa de implementação. Isso é diferente de uma falha no comando **verificar**. Não execute todas as práticas para conferir a instalação.

## 4. Estudar uma aula

1. Abra o `CONCEITO.md` indicado por `continuar` ou pelo [índice](estudos/README.md).
2. Leia o `PRATICA.md` da mesma aula, especialmente o contrato e a tabela dos casos.
3. Abra `pratica.py` e os arquivos adicionais indicados. Complete somente a prática.
4. Salve e execute os testes da aula:

   ```bash
   python3 estudar.py testar
   ```

   No Windows: `py -3 estudar.py testar`. Para uma aula específica, acrescente o número: `testar 05`.
5. Se falhar, identifique o caso, compare com o enunciado, corrija e teste novamente. Não é preciso enviar uma mensagem para IA.
6. Com os testes verdes, confira o checklist de autoavaliação da prática. Depois registre:

   ```bash
   python3 estudar.py concluir --revisei
   ```

   No Windows: `py -3 estudar.py concluir --revisei`. O comando executa os testes novamente; só salva a conclusão se todos os casos obrigatórios passarem, sem testes pulados.
7. A partir da aula 02, revise `git status`, `git diff` e faça um commit pequeno da sua prática. Nos checkpoints, sincronize sua própria cópia no GitHub, se configurada. [Roteiro Git](docs/GIT.md).

O avanço respeita a ordem e os checkpoints. Todos os materiais podem ser lidos a qualquer momento. Testar uma aula futura não altera sua posição e não libera seus pré-requisitos.

## Comandos de consulta

Nos exemplos abaixo, troque `python3` por `py -3` no Windows.

| Comando | Finalidade |
|---|---|
| `python3 estudar.py` | Retomar a aula atual. |
| `python3 estudar.py listar` | Ver as 32 aulas e sua situação. |
| `python3 estudar.py status` | Conferir o progresso e a posição. |
| `python3 estudar.py aula 18` | Consultar uma aula sem alterar o progresso. |
| `python3 estudar.py testar 18` | Executar somente os casos da aula 18. |
| `python3 estudar.py testar --concluidas` | Testar novamente as aulas registradas no progresso. |
| `python3 estudar.py testar --todas` | Executar todas as práticas; aulas não implementadas vão falhar. |
| `python3 estudar.py concluir --revisei` | Avaliar e concluir apenas a aula atual. |
| `python3 estudar.py verificar` | Conferir o sistema e os vínculos dos materiais. |
| `python3 estudar.py --help` | Consultar a ajuda dos comandos. |

Não há um comando de pular aulas ou de resolver exercícios automaticamente. Você pode revisar qualquer conteúdo sem alterar a sequência.

## Pastas e o que editar

```text
dev_learning_python/
├── estudar.py                  # comandos da trilha
├── estudos/                    # conceitos completos, por módulo e aula
├── praticas/                   # seus exercícios e enunciados
│   └── aulaNN_assunto/
│       ├── PRATICA.md          # contrato e tabela de casos
│       └── pratica.py          # TODOs para você implementar
├── testes/                     # casos públicos das práticas
├── testes_sistema/             # verificações do funcionamento da trilha
├── curriculum/                 # ordem, pré-requisitos e integridade
├── sistema/                    # executor e controle de progresso
├── docs/                       # guias de apoio e do professor
└── .learning/                  # criado ao concluir; estado pessoal ignorado pelo Git
```

Edite os arquivos indicados em `praticas/`. Na aula 27, o seu arquivo `test_pratica.py` também faz parte do exercício. Os testes de avaliação ficam em `testes/` e não devem ser alterados para fazer uma tentativa passar. O executor detecta alterações acidentais nesses arquivos.

O progresso fica em `.learning/progress.json`; a última conclusão e o histórico de conclusões ficam na mesma pasta. **Git não sincroniza esse progresso pessoal.** Para trocar de computador levando sua posição, copie `.learning/` separadamente junto da mesma versão das práticas. Há backup do estado anterior em `.learning/progress.json.bak`. [Retomada e recuperação](docs/PROGRESSO.md).

Se editar uma prática já concluída, ela volta a exigir validação e os pré-requisitos seguintes ficam pendentes. Ao reconcluí-la, as conclusões posteriores precisam ser registradas novamente. Seus arquivos de prática são preservados.

## O que uma aprovação significa

Os testes verificam os comportamentos publicados, e o checklist registra sua autoavaliação. Eles não provam compreensão, autoria, qualidade de todo algoritmo ou que você executou os comandos Git. Não há avaliação escondida nem análise por IA. O professor pode revisar o trabalho humano quando quiser; isso não é necessário para usar os comandos da trilha.

O executor executa código Python local, como qualquer programa que você escreve. Ele não é uma sandbox nem uma plataforma de exame contra adulteração intencional. O limite padrão é de 45 segundos por suíte de aula.

## Problemas frequentes

| Sintoma | Próximo passo |
|---|---|
| `python3` ou `py` não encontrado | Reabra o terminal após instalar e confira a seção do seu sistema operacional. |
| `can't open file estudar.py` | Entre com `cd` na pasta do clone; caminhos com espaços devem ficar entre aspas. |
| `No module named ...` | Execute a partir da raiz e use o mesmo Python que passou em `ambiente`. |
| `NotImplementedError` | Complete o TODO na prática correspondente; a estrutura inicial ainda não é uma solução. |
| `FAIL` ou `ERROR` | Leia [Como ler testes](docs/COMO_LER_TESTES.md) e o caso identificado no enunciado. |
| Teste ultrapassou 45 segundos | Verifique laço infinito, input indevido ou espera sem término. |
| Avaliação alterada ou progresso inválido | Siga [recuperação do progresso e dos arquivos](docs/PROGRESSO.md); preserve sua prática. |

## Distribuição e licença

O projeto foi preparado para ser publicado como repositório ou template pelo professor. A criação da pasta local não publica automaticamente no GitHub. Consulte [o guia de distribuição](docs/PROFESSOR.md) antes de enviar a URL aos alunos.

A licença segue a divisão entre área do aluno e núcleo da trilha em [LICENSE.md](LICENSE.md). [Registro de validação desta edição](docs/VALIDACAO.md).

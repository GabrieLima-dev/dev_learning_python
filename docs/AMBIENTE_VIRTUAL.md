# Ambiente virtual opcional

Um ambiente virtual mantém o interpretador e pacotes de um projeto separados de outros ambientes. Esta trilha não exige pacotes externos, mas você pode criar um para praticar essa organização. A pasta `.venv/` já está no gitignore.

No macOS/Linux, na raiz:

```bash
python3 -m venv .venv
.venv/bin/python estudar.py ambiente
.venv/bin/python estudar.py continuar
```

No Windows:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe estudar.py ambiente
.venv\Scripts\python.exe estudar.py continuar
```

Usar o caminho do executável evita precisar ativar o ambiente ou mudar políticas do PowerShell. Substitua o início dos demais comandos por esse mesmo executável.

No Ubuntu/Debian, se venv não estiver disponível, instale o pacote `python3-venv` pelo gerenciador da distribuição. O estudo sem ambiente virtual continua possível se ambiente confirmar as bibliotecas necessárias.

Não copie `.venv/` para outra máquina. Recrie-o a partir do Python instalado nela. Não é necessário executar pip install neste projeto.

Referência: [documentação oficial de venv](https://docs.python.org/3/library/venv.html).

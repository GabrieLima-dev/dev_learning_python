# Registrar a evolução com Git

Use sua própria cópia do repositório para guardar as soluções. Um clone do professor pode ser usado localmente, mas o endereço origin normalmente aponta para o repositório dele e você não terá permissão para enviar alterações.

Se Git pedir sua identidade para o primeiro commit, configure seus próprios dados **neste repositório**:

```bash
git config user.name "SEU NOME"
git config user.email "SEU EMAIL"
```

Substitua os textos pelos dados que deseja associar aos commits. Se usa um e-mail privado de contribuição do GitHub, copie o endereço fornecido pela sua conta. Não é necessário usar a opção global para praticar neste projeto.

## Após uma aula

```bash
git status
git diff
```

Leia as mudanças. Prepare apenas os arquivos da prática concluída, por exemplo:

```bash
git add praticas/aula05_textos/pratica.py
git diff --staged
git commit -m "Conclui pratica de textos"
```

Em atividades com vários arquivos, inclua os caminhos correspondentes. Evite adicionar toda a pasta indiscriminadamente. Não inclua bancos pessoais, caches, senhas, ambientes virtuais ou a pasta `.learning/`.

## Nos checkpoints

Confira o histórico e o destino:

```bash
git log --oneline -5
git remote -v
git status
```

Se origin é **sua cópia** e a branch já tem acompanhamento remoto, execute `git push`. Se ela ainda não tem acompanhamento, use `git push -u origin NOME_DA_SUA_BRANCH`, substituindo o nome pelo mostrado em `git branch --show-current`. Não envie para o repositório do professor sem combinar esse fluxo com ele.

Se o envio for rejeitado por divergência, pare para entender quais commits existem em cada lado. Não use force como tentativa de resolver automaticamente. Revise o fluxo com seu professor quando necessário.

Os comandos da trilha nunca fazem commit ou push. O teste da aula 02 confere respostas sobre Git; não atesta a realização desses passos. Seu checklist registra essa parte da prática.

Referências: [documentação do Git](https://git-scm.com/docs) e [livro Pro Git](https://git-scm.com/book/pt-br/v2).

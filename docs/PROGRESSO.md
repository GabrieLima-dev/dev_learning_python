# Progresso, retomada e recuperação

`continuar` e `status` leem o estado; não criam uma conclusão. `testar` só executa testes. `concluir --revisei` avalia a aula atual, exige todos os casos obrigatórios sem skips e salva a conclusão se você confirmou o checklist.

## Arquivos pessoais

A pasta `.learning/` é criada na primeira tentativa de conclusão e contém:

- `progress.json`: conclusões em ordem e assinaturas dos arquivos avaliados.
- `progress.json.bak`: cópia do estado anterior à última conclusão bem-sucedida, a partir da segunda gravação.
- `session.md`: resumo da última conclusão bem-sucedida.
- `history.md`: histórico de conclusões, sem diário de erros.
- `conclusao.lock`: existe somente enquanto uma conclusão está em andamento.

As datas são armazenadas em UTC para manter consistência entre computadores. O código do aluno nunca é reescrito por esses comandos.

## Editar uma aula já concluída

A assinatura inclui os arquivos declarados da prática e seus módulos Python adicionais. Se você editar um deles, mesmo um comentário, a primeira aula modificada passa a ser a atual e as posteriores aguardam revalidação. Os registros antigos permanecem no arquivo até você concluir novamente; nesse momento, somente a sequência validada é preservada. Os códigos e textos que você escreveu continuam no lugar.

Isso evita que o status apresente uma avaliação antiga como se correspondesse ao código atual. Não exige refazer sua implementação: rode os testes e conclua novamente em ordem. No projeto final, editar o README da entrega também exige reconcluir.

## Trocar de computador

Faça um commit das suas práticas e obtenha essa mesma versão na outra máquina. Copie separadamente a pasta `.learning/` para a raiz do novo clone, pois ela é ignorada pelo Git. Não copie ambiente virtual nem caches. Execute ambiente e status. Caso tenha alterado arquivos entre as cópias, o sistema solicitará revalidação.

## Progresso inválido

Um JSON inválido ou com estrutura incompatível produz mensagem de erro e é preservado. O programa não zera seu estado silenciosamente.

1. Feche comandos de conclusão em andamento.
2. Faça uma cópia da pasta `.learning/` em um local de sua escolha.
3. Se `progress.json.bak` existir e estiver íntegro, copie-o sobre `progress.json` pelo gerenciador de arquivos. Você recuperará o estado anterior à última conclusão.
4. Execute status. Se não há backup utilizável, renomeie a pasta `.learning/` inteira para um nome de backup fora do repositório. O próximo uso começará sem conclusões; suas práticas continuam preservadas, e você poderá revalidá-las em ordem.

Não edite os registros manualmente para simular aprovações. Os testes e a autoavaliação são o caminho normal de conclusão.

## Trava após interrupção

Se a mensagem disser que já há uma conclusão, confira se outro terminal ainda está executando o comando. Aguarde ou encerre esse processo primeiro. Apenas quando tiver certeza de que não há conclusão ativa, remova o arquivo `.learning/conclusao.lock` pelo gerenciador de arquivos. Não apague a pasta inteira para resolver apenas uma trava.

## Arquivos de avaliação alterados

`curriculum/integridade.json` registra as assinaturas dos testes públicos, executor e currículo. Isso detecta alterações acidentais e evita concluir com uma suíte diferente da distribuída. Não é uma proteção contra adulteração deliberada.

Se você alterou esses arquivos por engano, guarde suas práticas e restaure **somente os caminhos indicados na mensagem** a partir do repositório original do professor ou de um clone novo. Não execute uma restauração geral que apague seu trabalho. O aluno não deve regenerar o manifesto para aceitar um teste removido.

O professor que está mantendo uma nova versão do sistema pode atualizar o manifesto depois de revisar os testes, conforme o [guia de manutenção](PROFESSOR.md). Alunos que desejam apenas resolver a atividade editam os arquivos indicados em praticas.

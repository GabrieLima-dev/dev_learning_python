# Guia do professor e de distribuição

Este projeto é uma trilha de estudo local pronta para distribuição. Os alunos não precisam de IA, conta em serviço de avaliação, servidor, chave de API ou instalação de dependências com pip. Você publica a pasta como repositório e compartilha a URL.

## Preparar a distribuição

1. Execute `python3 estudar.py ambiente` e `python3 estudar.py verificar` na raiz (Windows: `py -3` no lugar de python3).
2. Confira que os arquivos de `praticas/` continuam com os esqueletos e TODOs destinados aos alunos. A aula 27 contém uma implementação propositalmente defeituosa para investigação, e a classe base da aula 25 já levanta NotImplementedError como parte do contrato.
3. Não inclua `.learning/`, ambientes virtuais, bancos pessoais, caches, credenciais nem cópias com soluções. O `.gitignore` contém os padrões locais.
4. Publique em um repositório da sua conta. Se deseja cópias independentes para alunos, marque-o como template nas configurações do GitHub. Consulte [criação de repositório](https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-new-repository) e [repositórios de modelo](https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-template-repository).
5. Copie a URL HTTPS publicada e envie aos alunos. O README usa um marcador explícito para essa URL e não aponta para um repositório presumido.
6. Confira a execução da automação no GitHub. A matriz preparada cobre Windows, macOS e Linux com Python 3.11 e 3.14, mas só será executada após publicação no serviço.

O clone deve manter a estrutura inteira. Não distribua apenas praticas: os conceitos, testes, currículo e executor fazem parte da experiência.

## Testes que devem passar numa cópia inicial

`estudar.py verificar` valida a estrutura, links locais e correspondência entre a tabela de casos e os testes. Depois executa `testes_sistema`, que confere o funcionamento da trilha em cópias temporárias. Esses testes devem passar antes de entregar o projeto.

As práticas **devem começar pendentes**. `estudar.py testar --todas` executa 32 suítes e vai falhar enquanto os alunos não implementarem as atividades. Não remova as falhas nem marque os exercícios como skip para deixar uma automação verde.

Os 149 casos públicos foram validados nesta edição contra implementações de referência em uma cópia temporária; essas soluções não fazem parte do material distribuído. Veja o [registro de validação](VALIDACAO.md). O professor pode manter sua própria cópia resolvida fora do repositório de alunos e executar nela:

```bash
python3 -m unittest discover -s testes -v
```

O teste da aula 27 executa também os testes escritos pelo aluno e verifica se eles detectam quatro regressões declaradas. O projeto final é testado tanto pela interface de objetos quanto por processos reais de terminal com banco temporário.

## O que a aprovação automática comprova

A conclusão exige a sequência de pré-requisitos, integridade dos avaliadores, término normal da suíte, todos os casos esperados executados sem falha ou skip e confirmação do checklist pelo aluno. Alterar uma prática concluída reabre sua validação.

Isso é um auxílio ao aprendizado, não uma plataforma resistente a adulteração. Não prova autoria nem compreensão. Os testes não verificam a realização de commits, sincronização com GitHub ou a qualidade textual do README final. Esses itens são autoavaliados ou revisados por você, se quiser uma avaliação humana.

## Adaptar uma atividade

Uma manutenção de conteúdo precisa manter quatro pontos alinhados:

1. O conceito ensina os recursos necessários antes de cobrá-los.
2. O enunciado informa domínio, entradas, retornos, efeitos, erros, mensagens, arredondamento e casos de fronteira.
3. Os esqueletos preservam as assinaturas e os TODOs explicam a tarefa sem entregar o algoritmo.
4. Os testes têm casos públicos correspondentes na tabela do enunciado, com soluções válidas passando e soluções incorretas relevantes falhando.

O currículo é `curriculum/python.json`. Seus IDs, pré-requisitos, caminhos, módulo de teste e quantidade de casos precisam corresponder aos arquivos reais. Ao acrescentar aulas, atualize também o índice, os números apresentados no README e as verificações da edição em testes_sistema.

Depois de revisar uma alteração legítima no núcleo, o mantenedor atualiza o manifesto:

```bash
python3 ferramentas/atualizar_integridade.py
python3 estudar.py verificar
```

No Windows, use `py -3`. Essa ferramenta não deve ser usada pelo aluno para contornar uma falha de integridade. As quebras de linha são fixadas em LF pelo `.gitattributes` para que as assinaturas não mudem no clone para Windows.

Teste a alteração em sua cópia resolvida e confirme que a cópia distribuída continua sem soluções. Execute também os exemplos Python dos conceitos em uma pasta temporária, especialmente os que criam arquivos. Mudanças no contrato durante uma turma devem ser comunicadas; não presuma que conclusões antigas equivalem à nova avaliação.

## Organização da turma

Cada aluno mantém sua própria pasta e seu próprio `.learning/`. O progresso não é sincronizado por Git. O sistema funciona sem identidade de aluno e sem coletar dados externos. Para receber trabalhos, combine um fluxo explícito com a turma, como compartilhar a URL da cópia pessoal ou entregar os arquivos da prática.

A revisão de um conteúdo pode ser feita por `aula N` e `testar N` sem alterar a posição. Não há diagnóstico obrigatório inicial, diário de erros, níveis automáticos de ajuda ou revisão espaçada. A aula 01 começa diretamente com a primeira prática.

## Licença

A distribuição preserva a autoria e o modelo de área do aluno/núcleo em [LICENSE.md](../LICENSE.md), adaptado aos caminhos desta trilha. Consulte os termos antes de redistribuir modificações do núcleo.

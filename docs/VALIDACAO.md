# Validação da edição inicial

Preparação local em 23/10/2026. Ambiente utilizado: macOS com Python 3.14.7. Este registro distingue os testes do sistema das atividades propositalmente incompletas dos alunos.

## Evidências

- 32 aulas com conceito, enunciado, arquivos de prática e suíte pública correspondente.
- 149 casos de avaliação executados com sucesso contra implementações de referência em uma cópia temporária, incluindo subprocessos do projeto final e persistência SQLite.
- Todas as 32 suítes dos esqueletos foram executadas e permaneceram pendentes; nenhuma aula foi aprovada sem implementação.
- O fluxo de 32 conclusões em sequência foi simulado com as referências, incluindo retomada no estado final. As soluções temporárias não foram incluídas no material distribuído.
- 35 exemplos Python dos conceitos verificados quanto à sintaxe e execução isolada.
- Vínculos locais dos documentos e IDs das tabelas de casos conferidos automaticamente.
- 22 testes do sistema passaram, tanto na cópia inicial quanto na cópia resolvida. Eles verificam retomada, conclusão, backup, falha sem avanço, revalidação, pré-requisitos, estado inválido, integridade, limite de duração e encerramento prematuro.

Para reproduzir a verificação que deve passar num clone inicial:

```bash
python3 estudar.py verificar
```

No Windows: `py -3 estudar.py verificar`.

## Limites da evidência

A validação local foi realizada no macOS. A configuração de GitHub Actions inclui Windows, Linux e macOS com Python 3.11 e 3.14; essa matriz precisa executar no repositório publicado para produzir evidência nessas outras combinações. Configuração de pipeline não equivale a execução confirmada.

As práticas incompletas não devem apresentar testes verdes. A verificação das referências foi feita em uma cópia separada e não é uma afirmação de que o aluno já concluiu os exercícios. Testes de comportamento e autoavaliação não comprovam entendimento, autoria ou realização das ações Git.

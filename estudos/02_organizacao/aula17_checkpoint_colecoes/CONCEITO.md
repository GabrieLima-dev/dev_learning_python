# 17 — Checkpoint: resumo de vendas

**Objetivo:** Consolidar registros em um relatório sem perder dados nem aceitar valores inválidos.

Este checkpoint combina registros, validação, funções e agregação. Uma venda individual informa um produto, sua quantidade e o preço unitário. O relatório reúne várias vendas do mesmo produto, preservando a identidade pelo nome exato.

A quantidade total e a receita total são acumuladores diferentes. Se um produto aparece com preços distintos, some a receita de cada venda; não multiplique toda a quantidade pelo último preço encontrado. Uma agregação correta não perde a contribuição dos registros anteriores.

Dados de entrada podem ser inválidos dentro do domínio descrito. O contrato pede rejeitar quantidade não positiva e preço negativo. Faça essa verificação de modo que os dados recebidos nunca sejam alterados, mesmo quando a falha está no meio da lista. Como o resultado é construído localmente e só devolvido ao fim, você pode evitar efeitos parciais externos.

A ordem das chaves de um dicionário não representa uma classificação. Nesta prática o teste compara o conteúdo do resumo, não a ordem visual. Se uma tela precisasse exibir os produtos alfabeticamente, essa seria outra responsabilidade.

Implemente por etapas: entenda um registro, depois um produto repetido, então vários produtos e por último os erros. Isso é uma sequência de investigação, não uma exigência de algoritmo. Use o estilo de funções e dados que consegue explicar. Ao terminar, revise seu histórico e sincronize sua cópia se usa GitHub.

## Exemplo comentado

```python
# Exemplo de formato de registro de outra aplicação:
leitura = {"sensor": "sala", "valor": 23}
print(leitura["sensor"], leitura["valor"])
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Calculei a receita por venda, inclusive quando o preço muda.
- [ ] Sei explicar como evitei modificar os dados de entrada.
- [ ] Revisei meu commit e sincronizei minha cópia no GitHub, se configurada.

Abra o [enunciado](../../../praticas/aula17_checkpoint_colecoes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula17_checkpoint_colecoes/pratica.py) e consulte o [teste público](../../../testes/test_aula17_checkpoint_colecoes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 17
```

```powershell
# Windows
py -3 estudar.py testar 17
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

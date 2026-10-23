# Como entender o que o teste aceita

Um teste faz uma chamada e compara o que aconteceu com o contrato. Os testes de avaliação estão na pasta `testes/` e cada método tem um identificador como `test_A07_02`. Procure **A07-02** na tabela de `praticas/aula07_decisoes/PRATICA.md`: essa linha explica a entrada, a saída e as condições verificadas.

## Exemplo de leitura

Considere um exemplo fora das práticas:

```python
self.assertEqual(duplicar(4), 8)
```

O teste chama duplicar com 4. A função precisa devolver 8. Imprimir 8 e devolver None não satisfaz essa verificação. O valor esperado foi escrito por quem definiu o contrato; a função do aluno calcula o valor real.

Os testes desta trilha também usam `assertValor`, definido em [testes/apoio.py](../testes/apoio.py). Ele compara valor e tipo, inclusive dentro de listas, tuplas e dicionários. `True` e `1` não são intercambiáveis. Floats usam tolerância absoluta e relativa de 1e-9, salvo comparação diferente explícita no próprio caso.

| Verificação | O que ela exige |
|---|---|
| `assertEqual(real, esperado)` | Igualdade entre os valores. |
| `assertValor(real, esperado)` | Igualdade de valor e tipo segundo as regras acima. |
| `assertIsNone(real)` | O resultado precisa ser None. |
| `assertIsNot(resultado, entrada)` | Os dois nomes não podem apontar para o mesmo objeto. |
| `assertRaises(ValueError)` | A chamada deve levantar essa exceção. Retornar texto de erro não basta. |
| Comparação da entrada após a chamada | A função deve preservar os dados recebidos. |
| Captura de stdout | O teste confere o texto impresso, incluindo espaços e `\n`. |
| Simulação de input | As respostas são fornecidas pelo teste; você não digita enquanto ele roda. |

## Diagnosticar uma falha

1. Leia a identificação do caso que falhou.
2. Abra a linha correspondente na tabela do enunciado.
3. No final do erro, veja se o problema é de sintaxe, uma exceção inesperada ou uma comparação.
4. Compare o valor esperado com o recebido. Verifique também tipo, espaços, acentos e quebras.
5. Faça uma correção pequena na prática, salve e execute o mesmo comando novamente.

Exemplo de saída resumida:

```text
FAIL: test_A07_02 (...)
AssertionError: 'reprovado' != 'recuperacao'
```

Nesse caso, investigue as fronteiras de classificação da nota. O teste não pede que você altere o texto esperado: pede que sua função cumpra a regra publicada.

`ERROR` significa que a chamada foi interrompida. `NotImplementedError` costuma indicar um TODO inicial ainda não resolvido. `SyntaxError` indica que Python não conseguiu interpretar a escrita; `NameError` pode indicar nome inexistente; `TypeError` pode indicar tipo inadequado. Depois de corrigir o primeiro erro, rode de novo: ele pode ter impedido que outros casos fossem avaliados.

## Categorias para sua investigação

- **SYNTAX:** escrita inválida, como falta de dois-pontos ou indentação incorreta.
- **LOGIC:** o código executa, mas calcula ou decide incorretamente.
- **CONCEPT:** a solução deixa de praticar o assunto, como devolver uma lista completa onde foi pedido um gerador gradual.
- **DESIGN:** responsabilidades ou estado estão organizados de forma que dificultam o uso, como compartilhar saldo entre contas.
- **GOOD_PRACTICE:** nomes pouco claros, repetição desnecessária ou ausência de revisão do diff.

O sistema não inventa automaticamente uma classificação pedagógica para cada falha. Use essas categorias para pensar na causa; o diagnóstico automático continua sendo a saída real do unittest.

## Evite contornar a atividade

Não remova asserts, não marque testes como skip e não altere o valor esperado. Não use respostas fixas reconhecendo as entradas dos exemplos. O contrato vale para todo o domínio declarado, mesmo que os testes só possam amostrar alguns casos.

Você pode ler todos os testes. Conhecer o contrato é parte do trabalho. A aula 27 ensina inclusive a escrever testes e conferir se eles detectam regressões. A única pasta em que você escreverá seus testes como atividade é `praticas/aula27_testes_debugging/`; os avaliadores permanecem em `testes/`.

Teste verde é evidência de comportamento. Antes de concluir, explique sua solução, faça a autoavaliação e confira se praticou o conceito da aula.

Referência: [documentação oficial do unittest](https://docs.python.org/3/library/unittest.html).

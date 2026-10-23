# 05 — Textos e formatação

**Objetivo:** Transformar textos e produzir uma mensagem com formato exato.

Strings são sequências de caracteres. Elas podem conter letras, números escritos como texto, espaços e acentos. Uma string não é modificada no lugar: métodos como `strip()` e `lower()` produzem outra string. Se você precisa usar o resultado, guarde ou devolva esse resultado.

`strip()` remove espaços em branco nas extremidades; não remove espaços entre palavras. `lower()` converte letras para minúsculas. `upper()` converte para maiúsculas. `replace(antigo, novo)` substitui ocorrências, e `len(texto)` informa o tamanho. A escolha do método depende da regra: normalizar um nome de usuário e exibir um nome próprio são necessidades diferentes.

Uma f-string começa com a letra `f` antes das aspas. Expressões entre chaves são avaliadas e incorporadas ao texto. Isso permite combinar texto e números sem usar `str()` para cada número. O resultado da f-string continua sendo uma string, não uma impressão automática.

Pontuação e espaços também fazem parte do resultado. Quando um teste espera `Item: Livro (2)`, `Item:Livro(2)` não é equivalente. Escreva o formato solicitado e deixe os valores variáveis nos lugares adequados. Não copie o nome de um exemplo como se fosse o único possível.

Nesta aula, separar normalização de formatação torna cada responsabilidade clara. A primeira função limpa extremidades e converte para minúsculas. A segunda exibe o produto exatamente como o recebeu: aplicar a mesma limpeza às duas funções violaria a especificação.

## Exemplo comentado

```python
cidade = "  MACEIÓ  "
normalizada = cidade.strip().lower()
print(normalizada)  # maceió
quantidade = 3
print(f"Visitas: {quantidade}")  # Visitas: 3
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Sei que os métodos de string devolvem um novo valor.
- [ ] Conferi os espaços, a pontuação e o comportamento com texto vazio.

Abra o [enunciado](../../../praticas/aula05_textos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula05_textos/pratica.py) e consulte o [teste público](../../../testes/test_aula05_textos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 05
```

```powershell
# Windows
py -3 estudar.py testar 05
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

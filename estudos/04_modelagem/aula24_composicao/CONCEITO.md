# 24 — Dataclasses e composição de objetos

**Objetivo:** Representar itens imutáveis e compor um carrinho com estado independente.

Uma dataclass reduz o trabalho repetitivo em classes que representam dados. O decorador `@dataclass` gera inicialização, representação e comparação usando campos anotados. A ordem dos campos define a ordem dos argumentos posicionais na inicialização gerada.

Com `frozen=True`, atribuições comuns aos campos são bloqueadas depois de criar o objeto. Isso é útil para representar um item cujo nome e preço não devem mudar no meio de um cálculo. Não é uma promessa de imutabilidade profunda para qualquer estrutura interna; nesta aula os campos são strings e inteiros, que já são imutáveis.

Composição é construir um objeto usando outros objetos. Um carrinho possui vários itens, e o item sabe calcular o próprio subtotal. O carrinho coordena a coleção e calcula o total. Essa divisão evita repetir a regra de subtotal em quem usa o item.

Coleções mutáveis precisam pertencer a cada instância. Iniciar uma lista dentro do construtor cria uma lista nova para cada carrinho. Se usasse dataclass para o carrinho, a ferramenta correspondente seria field(default_factory=list). Escolha a forma que consegue explicar.

As anotações de tipo não validam automaticamente preços e quantidades. Para manter o foco, o contrato garante entradas válidas. Uma futura regra de rejeição deve ser adicionada de forma explícita, com casos de teste próprios, em vez de ser presumida porque existe uma anotação.

## Exemplo comentado

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Endereco:
    cidade: str
    numero: int

casa = Endereco("Maceió", 12)
print(casa.cidade)
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Usei a dataclass para representar dados e o carrinho para coordenar itens.
- [ ] O carrinho usa subtotal dos itens e cada carrinho tem sua coleção.

Abra o [enunciado](../../../praticas/aula24_composicao/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula24_composicao/pratica.py) e consulte o [teste público](../../../testes/test_aula24_composicao.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 24
```

```powershell
# Windows
py -3 estudar.py testar 24
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

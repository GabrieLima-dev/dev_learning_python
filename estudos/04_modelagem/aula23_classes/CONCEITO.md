# 23 — Classes, objetos e estado

**Objetivo:** Implementar uma conta com estado independente e validações antes de movimentar.

Uma classe define um tipo que reúne dados e comportamentos. Um objeto é uma instância dessa classe, com seu próprio estado. `__init__` inicializa o objeto; `self` identifica a instância na qual o método está atuando.

Atributos como `self.titular` pertencem ao objeto. Duas contas devem manter saldos independentes. Usar um atributo de classe para um estado que deveria ser individual pode fazer dados vazarem de uma instância para outra.

Um método é uma função definida dentro da classe. Ao chamar `conta.depositar(100)`, Python fornece a própria conta como self. O método pode consultar ou modificar seus atributos. O contrato precisa explicar se ele devolve algo além de mudar o estado.

Regras que devem permanecer verdadeiras são invariantes. Nesta prática o saldo nunca fica negativo e valores de movimentação devem ser positivos. Valide a operação antes de modificar o saldo. Uma tentativa rejeitada deve manter a conta exatamente como estava.

Encapsular não significa apenas esconder atributos. Significa concentrar as regras no lugar que protege o estado. Por simplicidade, titular e saldo são públicos nesta aula, mas os métodos devem ser usados para as movimentações. A autoavaliação inclui não contornar os métodos alterando saldo diretamente para fazer um teste passar.

Compare a modelagem com os dicionários das aulas anteriores: ambos guardam dados, mas a classe oferece operações próprias e pode manter regras junto desses dados. Use classes quando essa união ajuda a expressar o problema.

## Exemplo comentado

```python
class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 1
        return self.valor

contador = Contador()
print(contador.incrementar())  # 1
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] O estado pertence à instância e não é compartilhado entre contas.
- [ ] Valido antes de modificar o saldo.

Abra o [enunciado](../../../praticas/aula23_classes/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula23_classes/pratica.py) e consulte o [teste público](../../../testes/test_aula23_classes.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 23
```

```powershell
# Windows
py -3 estudar.py testar 23
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

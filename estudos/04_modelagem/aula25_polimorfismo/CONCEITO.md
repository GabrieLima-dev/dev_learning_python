# 25 — Herança e polimorfismo

**Objetivo:** Implementar uma hierarquia pequena e consumir objetos pela operação que oferecem.

Herança permite definir uma classe como especialização de outra. A classe derivada recebe métodos da classe base e pode redefinir comportamentos. `super()` permite chamar a implementação da classe base, por exemplo, para reaproveitar sua inicialização.

Polimorfismo significa usar objetos diferentes por uma mesma operação. Se vários objetos oferecem `area()`, uma função pode pedir a área de cada um sem conhecer todos os seus tipos concretos. Em Python, frequentemente basta o objeto cumprir essa interface; isso é conhecido como duck typing.

Evite transformar uma função genérica numa lista de testes de tipo. Se a função faz `isinstance` para cada forma conhecida, uma nova forma exigiria modificar a função. Pedir diretamente a operação combinada permite acrescentar formas sem alterar quem soma as áreas.

Nesta atividade, a classe base informa que uma área ainda não está implementada levantando NotImplementedError. Esse é um uso real de projeto para a mesma exceção que usamos nos esqueletos. Nos exercícios comuns ela deve desaparecer das partes concluídas; na classe base desta aula ela é exatamente o comportamento pedido.

Herança não é obrigatória para todo reaproveitamento. O carrinho da aula anterior possui itens, por isso composição fazia sentido. Já um quadrado é modelado aqui como um retângulo com lados iguais, o que permite experimentar a relação de especialização sem adicionar propriedades mutáveis que complicariam essa regra.

## Exemplo comentado

```python
class Som:
    def tocar(self):
        raise NotImplementedError

class Sino(Som):
    def tocar(self):
        return "dim"

print(Sino().tocar())
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Sei explicar a diferença entre possuir um objeto e especializar uma classe.
- [ ] total_areas aceita uma nova forma sem precisar conhecer o tipo dela.

Abra o [enunciado](../../../praticas/aula25_polimorfismo/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula25_polimorfismo/pratica.py) e consulte o [teste público](../../../testes/test_aula25_polimorfismo.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 25
```

```powershell
# Windows
py -3 estudar.py testar 25
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

# 27 — Escrita de testes e investigação de falhas

**Objetivo:** Corrigir um limite e escrever testes que detectam regressões reais.

Até aqui você executou testes prontos. Agora escreverá seus próprios testes com unittest. Uma classe herda de unittest.TestCase e métodos cujo nome começa com test_ representam casos. Dentro deles, assertEqual compara resultados e assertRaises verifica uma exceção esperada.

Organize cada teste em preparação, ação e verificação. Prepare a entrada, chame a operação e confira uma consequência relevante. Não escreva um teste que repete o mesmo algoritmo da função para descobrir o resultado esperado: uma falha na regra poderia ser duplicada nos dois lugares.

Fronteiras são bons alvos. Se uma regra muda em 20000 centavos, verifique abaixo, exatamente no limite e acima. Um caso no meio da faixa pode passar mesmo quando o operador da comparação está errado. A suíte desta aula contém um defeito proposital para você investigar.

Teste de regressão é aquele que falha por causa de um defeito conhecido e continua protegendo a regra depois da correção. Primeiro reproduza a falha, leia o resultado, localize a condição responsável, faça uma correção pequena e execute novamente.

Para verificar a qualidade dos testes que você escreveu, a avaliação troca temporariamente a função por versões defeituosas. Seus testes precisam detectar cada uma. Isso se chama teste por mutação. Não se trata de código escondido: todas as versões defeituosas estão descritas na prática e visíveis no teste público. O módulo de prática é restaurado após cada simulação.

Importe o módulo pratica, como no esqueleto, e faça as chamadas por `pratica.frete`. Uma importação direta da função manteria uma referência antiga e impediria a troca usada nesta aula.

## Exemplo comentado

```python
import unittest

class TesteExemplo(unittest.TestCase):
    def test_texto_em_maiusculas(self):
        self.assertEqual("oi".upper(), "OI")
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Observei um teste falhar antes de corrigir a função.
- [ ] Meus testes têm resultados esperados explícitos e detectam as quatro regressões.
- [ ] Consigo explicar a causa do erro, além de apontar a linha alterada.

Abra o [enunciado](../../../praticas/aula27_testes_debugging/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula27_testes_debugging/pratica.py) e consulte o [teste público](../../../testes/test_aula27_testes_debugging.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 27
```

```powershell
# Windows
py -3 estudar.py testar 27
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

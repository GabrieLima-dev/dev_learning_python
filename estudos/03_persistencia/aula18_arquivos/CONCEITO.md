# 18 — Arquivos de texto e caminhos

**Objetivo:** Salvar e recuperar linhas de texto usando caminhos recebidos como argumento.

Dados guardados apenas em variáveis desaparecem quando o programa termina. Arquivos permitem persistir informação. Um caminho identifica onde o arquivo está. A classe Path, do módulo pathlib, oferece operações que funcionam com os separadores de caminho de cada sistema operacional.

Um arquivo de texto tem uma codificação. Use UTF-8 explicitamente para que nomes com acentos tenham a mesma interpretação em máquinas diferentes. O modo `r` lê, `w` escreve substituindo o conteúdo anterior, e `a` acrescenta ao final. Escolher o modo errado pode manter dados antigos ou apagar conteúdo que deveria ser preservado.

O bloco `with` fecha o arquivo mesmo se uma operação falhar. Métodos como `Path.read_text` e `Path.write_text` também gerenciam a abertura e o fechamento. Para lidar com linhas, lembre que a quebra de linha faz parte do conteúdo gravado, mas pode ser removida ao dividir o texto em linhas.

Um arquivo inexistente provoca FileNotFoundError em uma leitura comum. Algumas aplicações tratam ausência como uma coleção vazia; outras precisam avisar. Nesta aula o enunciado escolhe coleção vazia. Não capture todos os erros de arquivo: falta de permissão é diferente de ausência.

As práticas recebem o caminho por parâmetro. Isso permite que os testes usem diretórios temporários e que o programa real escolha outro local. Não fixe caminhos do seu computador no código. O diretório pai já existe e não é necessário criá-lo nesta atividade. Para gravar exatamente as quebras LF (`\n`) do contrato também no Windows, use `newline="\n"` na abertura ou em write_text; sem essa opção a escrita de texto pode traduzir as quebras para o formato do sistema.

## Exemplo comentado

```python
from pathlib import Path

caminho = Path("anotacao.txt")
# Exemplo para experimentar em uma pasta de rascunho:
caminho.write_text("Café\n", encoding="utf-8", newline="\n")
texto = caminho.read_text(encoding="utf-8")
print(texto)
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] O caminho vem do argumento e não está fixado na minha máquina.
- [ ] Sei por que devo escolher UTF-8 e distinguir arquivo ausente de outros erros.

Abra o [enunciado](../../../praticas/aula18_arquivos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula18_arquivos/pratica.py) e consulte o [teste público](../../../testes/test_aula18_arquivos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 18
```

```powershell
# Windows
py -3 estudar.py testar 18
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

# 29 — HTTP, URLs e contratos de resposta

**Objetivo:** Codificar parâmetros de URL e interpretar respostas segundo um contrato explícito.

HTTP é um protocolo de troca de mensagens entre cliente e servidor. Uma requisição informa método, endereço, cabeçalhos e, às vezes, corpo. Uma resposta informa um código de status e pode trazer um corpo. O significado dos dados depende do contrato da aplicação.

Uma URL pode conter parâmetros de consulta após um ponto de interrogação. Não monte esses parâmetros concatenando valores arbitrários: espaços, acentos e símbolos precisam ser codificados. `urllib.parse.urlencode` transforma um dicionário em uma consulta apropriada. `parse_qs` faz a interpretação inversa e é útil para testar o resultado sem depender da ordem textual dos parâmetros.

Um código de sucesso e um corpo JSON são informações distintas. Um servidor pode responder com status 200, mas enviar JSON malformado. O cliente deve detectar o problema ao interpretar o corpo. Já um status de erro pode significar que o corpo nem deve ser tratado como dados do domínio.

Nesta prática usamos uma política didática explícita: 200 interpreta JSON, 404 representa ausência e os outros códigos levantam um erro. Isso não é uma regra universal de todas as APIs. Cada integração real precisa documentar os códigos e formatos que aceita.

A atividade funciona sem internet. Você implementará a transformação de endereço e a interpretação de uma resposta recebida, separadas da conexão de rede. Essa divisão torna testes rápidos e previsíveis. Requisições reais, autenticação, retries e servidores web ficam fora desta trilha.

## Exemplo comentado

```python
from urllib.parse import urlencode

consulta = urlencode({"cidade": "São Paulo", "pagina": "1"})
print(consulta)  # cidade=S%C3%A3o+Paulo&pagina=1
```

Leia o exemplo, preveja a saída e só depois experimente. Ele ilustra o assunto; a tarefa e seus critérios estão no enunciado da prática.

## Antes de seguir

- [ ] Codifiquei os parâmetros com a biblioteca em vez de concatenar os valores.
- [ ] Sei distinguir erro de status e erro de sintaxe do corpo.

Abra o [enunciado](../../../praticas/aula29_http_contratos/PRATICA.md), implemente no [arquivo Python](../../../praticas/aula29_http_contratos/pratica.py) e consulte o [teste público](../../../testes/test_aula29_http_contratos.py).

Execute os testes ao terminar, a partir da raiz:

```bash
# macOS ou Linux
python3 estudar.py testar 29
```

```powershell
# Windows
py -3 estudar.py testar 29
```

Os casos automáticos confirmam os comportamentos especificados. Use o checklist para conferir sua compreensão. Consulte também [como ler uma falha](../../../docs/COMO_LER_TESTES.md).

[Voltar ao índice completo](../../README.md)

# Etapa 2 — Validação de portas de rede

## Problema

Uma ferramenta de diagnóstico de rede precisa receber uma porta válida antes de tentar abrir uma conexão TCP. Sem validação, valores como `0`, `65536` ou `"443"` podem gerar falhas confusas durante a execução.

## Regra implementada

A função `is_valid_port(port)` retorna:

- `True` para números inteiros entre `1` e `65535`;
- `False` para portas fora desse intervalo;
- `False` para valores que não sejam números inteiros.

## Por que 1 a 65535?

Portas TCP e UDP são identificadores numéricos de 16 bits sem sinal. Por isso, o intervalo tecnicamente válido vai de 1 até 65535.

## Arquivos envolvidos

| Arquivo | Responsabilidade |
| --- | --- |
| `src/it_ops_toolkit/network.py` | Implementa a regra de validação |
| `tests/test_network.py` | Verifica o comportamento esperado |

## Cenários testados

| Entrada | Resultado esperado | Motivo |
| --- | --- | --- |
| `443` | `True` | Porta HTTPS válida |
| `0` | `False` | Fora do intervalo válido |
| `65536` | `False` | Acima do limite de 16 bits |
| `"443"` | `False` | Texto não é uma porta numérica |

## Validação executada

```bash
python -m pytest -v
python -m ruff check .

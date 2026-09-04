# Verificador de porta TCP

## Objetivo

Disponibilizar um diagnóstico simples para confirmar se um host aceita conexões TCP em uma porta específica.

Esse tipo de verificação ajuda em troubleshooting de serviços como:

- HTTPS na porta 443;
- HTTP na porta 80;
- SSH na porta 22;
- banco de dados e aplicações internas em portas específicas.

## O que foi implementado

A Sprint 2 adicionou:

- validação de portas TCP/UDP entre `1` e `65535`;
- função `check_tcp_port`, que tenta abrir uma conexão TCP;
- tratamento de host, porta e timeout inválidos;
- retorno `True` para conexão bem-sucedida e `False` para falha;
- comando de terminal `check-port`;
- testes automatizados para lógica de rede e interface de linha de comando.

## Decisão técnica

Foi utilizada a função `socket.create_connection` da biblioteca padrão do Python.

A escolha evita dependências externas e permite definir um timeout para não deixar o diagnóstico aguardando indefinidamente.

Fluxo da execução:

```text
Comando CLI -> valida parâmetros -> tenta conexão TCP -> exibe resultado -> retorna código de saída

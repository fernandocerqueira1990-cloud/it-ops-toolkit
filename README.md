# IT Ops Toolkit

Laboratório prático em **Python** para automação, diagnóstico e operações de TI.

Este projeto será construído passo a passo. Cada avanço registra o **objetivo**, a **decisão técnica**, o **motivo** e a forma de **validar** o resultado.

## Objetivo

Criar ferramentas de linha de comando para apoiar uma operação de TI em tarefas como:

- verificar conectividade e portas TCP;
- consultar recursos básicos de um servidor;
- gerar relatórios para troubleshooting;
- praticar código testável, documentado e versionado.

O cenário usa problemas reais de operações N2/N3 como base, transformando experiência em infraestrutura, redes e observabilidade em software reutilizável.

## Tecnologias previstas

Python 3.13, Pytest, Ruff, Git/GitHub e GitHub Actions. Nas próximas etapas, também serão explorados logs estruturados, configuração por arquivo e relatórios CSV/JSON.

## Como aprenderemos

Não vamos apenas executar comandos. Para cada etapa, responderemos:

1. **Qual problema estamos resolvendo?**
2. **Como a solução funciona?**
3. **Por que esta escolha técnica foi feita?**
4. **Como verificamos que funciona?**

Consulte [docs/00-backlog.md](docs/00-backlog.md) para acompanhar o roteiro.

A primeira funcionalidade entregue está documentada em
[Verificador de porta TCP](docs/01-tcp-port-check.md).

- [x] Verificador de conectividade TCP implementado
- [x] Interface de linha de comando criada
- [x] Testes automatizados da funcionalidade executados
- [x] Documentação da funcionalidade adicionada

## Estado atual

- [x] Repositório e estrutura-base criados
- [x] Ambiente virtual Python configurado
- [x] Pytest e Ruff instalados
- [x] Primeiro módulo: validação de portas de rede
- [x] Primeiros testes automatizados executados
- [x] Documentação da funcionalidade criada
- [x] Primeiro commit e publicação no GitHub concluídos

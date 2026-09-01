# Etapa 1 — Fundação do projeto

## Problema que estamos resolvendo

Antes de escrever uma ferramenta de diagnóstico, precisamos de um ambiente previsível. Sem isso, o código pode funcionar somente em uma máquina, depender de bibliotecas instaladas por acaso ou ser difícil de testar.

## Decisões técnicas

### Python 3.12

Python tem sintaxe legível e é muito usado em automação, APIs, dados e infraestrutura. Isso permite focar no raciocínio de programação e em problemas reais de operações.

### Ambiente virtual (`.venv`)

Um ambiente virtual isola as bibliotecas deste projeto. Assim, instalar uma versão de Pytest aqui não altera outros projetos nem o Python do sistema.

### `pyproject.toml`

É o arquivo padrão moderno para concentrar os metadados do projeto e a configuração de ferramentas. Ele informa, por exemplo, qual versão mínima de Python aceitamos e onde os testes ficam.

### Estrutura `src/`

O código da aplicação ficará em `src/it_ops_toolkit/`. Separá-lo de testes e documentos é uma convenção profissional e reduz importações acidentais durante o desenvolvimento.

### `.gitignore`

Git deve registrar código, documentação e configurações reproduzíveis — não arquivos temporários, caches, bibliotecas locais ou segredos. Esse arquivo define explicitamente o que não será versionado.

## Estrutura final desta etapa

```text
it-ops-toolkit/
├── docs/                 # decisões, guias e backlog
├── src/it_ops_toolkit/   # código reutilizável
├── tests/                # testes automatizados
├── .gitignore            # exclusões do Git
├── pyproject.toml        # configuração do projeto
└── README.md             # visão geral
```

## Critério de conclusão

A fundação estará concluída após:

1. criar as pastas `src/` e `tests/`;
2. criar e ativar o ambiente virtual;
3. instalar ferramentas de desenvolvimento;
4. executar um primeiro teste automatizado.

A próxima etapa fará isso com cada comando explicado antes de ser usado.

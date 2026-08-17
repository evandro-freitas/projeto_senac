# Missão dos alunos

Vocês assumiram a manutenção da API da **JP Solutions**.

A direção não informou exatamente onde estão os defeitos. A investigação faz parte da atividade.

## Etapa 1 — Diagnóstico

Antes de alterar código:

- execute a aplicação;
- acesse `/docs`;
- teste as rotas;
- execute `pytest -q`;
- observe os status codes;
- leia mensagens de erro;
- registre comportamentos suspeitos.

## Etapa 2 — Issue

Cada problema deve virar uma Issue própria.

Uma boa Issue deve conter:

- título;
- comportamento observado;
- passos para reproduzir;
- comportamento esperado;
- evidências;
- critérios de aceite.

## Etapa 3 — Branch

Crie uma branch por problema.

Exemplos:

```text
fix/12-status-cursos
fix/15-filtro-cursos
fix/21-permissao-admin
```

## Etapa 4 — Correção

Evite mudar arquivos sem relação com a Issue.

Execute os testes antes de abrir o PR.

## Etapa 5 — Pull Request

O PR deve informar:

- o que foi alterado;
- por que foi alterado;
- Issue relacionada;
- como testar;
- evidências.

## Etapa 6 — Code Review

O reviewer deve verificar:

- se os critérios de aceite foram atendidos;
- se os status codes fazem sentido;
- se a correção criou outro problema;
- se há mudanças fora do escopo;
- se os testes passam;
- se a pipeline está verde.

## Regra principal

Não vale pesquisar por uma lista pronta de bugs.

O objetivo é aprender a investigar.

Alunos: Andre Bernardino, Evandro José de Freitas, João Antunes, Jeferson Macedo, Renan Mateus, Patrick dos Santos, João Gabriel

# JP Solutions — FastAPI DevOps Lab

Laboratório educacional para praticar:

- Git em equipe;
- Issues;
- branches;
- Conventional Commits;
- Pull Requests;
- Code Review;
- CI com GitHub Actions;
- testes automatizados;
- investigação de bugs;
- HTTP e Status Codes.

> O projeto contém problemas intencionais. O objetivo não é apenas corrigir o código, mas investigar e resolver cada problema seguindo um fluxo profissional.

## Contexto

A JP Solutions mantém uma pequena API de cursos.

A equipe anterior entregou o sistema sem processo consistente e surgiram reclamações:

- respostas HTTP incoerentes;
- dados incorretos na listagem;
- validações ausentes;
- problemas de autorização;
- pipeline de CI falhando.

Sua equipe assumirá a manutenção.

## Tecnologias

- Python
- FastAPI
- Pytest
- GitHub Actions

Nenhum conhecimento de HTML, CSS ou JavaScript é necessário.

## Como executar

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
uvicorn app.main:app --reload
```

Acesse:

```text
http://127.0.0.1:8000/docs
```

O Swagger permite testar todas as rotas sem frontend.

## Testes

```bash
pytest -q
```

É esperado que alguns testes falhem no estado inicial.

> Não altere um teste válido apenas para deixá-lo verde. Descubra primeiro se o comportamento da aplicação está incorreto.

## Tokens simulados

Aluno:

```text
Bearer token-aluno
```

Administrador:

```text
Bearer token-admin
```

No Swagger, adicione o header `Authorization` quando necessário.

## Fluxo obrigatório

```text
Problema
   ↓
Investigar
   ↓
Issue
   ↓
Branch
   ↓
Correção
   ↓
Pytest
   ↓
Commit
   ↓
Pull Request
   ↓
Code Review
   ↓
GitHub Actions
   ↓
Merge
```

Leia também:

- `CONTRIBUTING.md`
- `docs/MISSAO_DOS_ALUNOS.md`

Boa investigação.

# Como contribuir

Este projeto simula o fluxo de uma equipe de desenvolvimento.

## Regras

1. Não desenvolva diretamente na `main`.
2. Toda correção deve estar relacionada a uma Issue.
3. Crie uma branch a partir da `main` atualizada.
4. Utilize nomes como:
   - `fix/12-status-cursos`
   - `fix/18-validacao-contato`
   - `docs/23-atualiza-readme`
5. Utilize Conventional Commits:
   - `feat:`
   - `fix:`
   - `docs:`
   - `refactor:`
   - `test:`
   - `chore:`
6. Abra um Pull Request.
7. O autor não deve aprovar o próprio PR.
8. A pipeline deve estar verde antes do merge.
9. Não misture problemas diferentes no mesmo PR.

## Exemplo

```bash
git checkout main
git pull

git checkout -b fix/18-validacao-contato

# desenvolver...

git add .
git commit -m "fix: valida campos obrigatórios do contato"
git push -u origin fix/18-validacao-contato
```

# Publicar no GitHub

```
1. Baixe o projeto como ZIP
```


Crie um repositório vazio no GitHub.

Depois:

```bash
git init
git add .
git commit -m "chore: adiciona versão inicial do laboratório"
git branch -M main
git remote add origin <URL_DO_REPOSITORIO>
git push -u origin main
```

## Configuração recomendada

Após publicar:

1. Abra as configurações do repositório.
2. Proteja a branch `main`, quando disponível.
3. Exija Pull Request antes do merge.
4. Exija pelo menos uma aprovação.
5. Exija a execução da CI antes do merge.

As opções disponíveis podem variar conforme o tipo de repositório e plano.

---
name: quartz-upgrade
description: >
  Guia completo para atualizar o Quartz v5 do upstream (jackyzha0/quartz ou
  quartz-community), resolver conflitos de merge e integrar as mudanças na
  branch principal (main) deste repositório jocile.github.io.
  Ativa quando o usuário mencionar: upgrade do quartz, atualizar quartz,
  npx quartz upgrade, conflito de merge no quartz, rebase v5, PR do quartz.
---

# Skill: Upgrade do Quartz v5

Este repositório usa o Quartz v5 com plugins da `quartz-community`.
A branch `v5` rastreia o upstream e é integrada ao `main` via PR com **Squash and merge**.

## Estrutura de branches

```
main        <- branch de produção (GitHub Pages)
v5          <- rastreia upstream/v5 (jackyzha0/quartz)
```

## Arquivos protegidos (NUNCA sobrescrever)

| Arquivo | Motivo |
|---|---|
| `quartz.config.yaml` | Configuração personalizada do site (tema, plugins, pt-BR) |
| `quartz.lock.json` | Lock dos plugins com especificadores `github:` |
| `.github/workflows/deploy.yml` | Workflow de deploy para GitHub Pages |
| `content/` | Todo o conteúdo do site |

## Passo a Passo do Upgrade

### 1. Executar o upgrade oficial

```powershell
git checkout v5
npx quartz upgrade
```

### 2. Fazer push e abrir PR

```powershell
git push origin v5
```

Abrir PR de `v5` → `main` no GitHub.

### 3. Verificar conflitos

```powershell
git status
git diff --name-only --diff-filter=U
```

### 4. Resolver conflitos (rebase)

```powershell
git fetch origin
git checkout v5
git rebase origin/main
```

#### 4a. quartz.config.yaml — SEMPRE manter local

```powershell
git checkout --ours quartz.config.yaml
git add quartz.config.yaml
git -c core.editor=true rebase --continue
```

#### 4b. quartz.lock.json — SEMPRE manter local

```powershell
git add quartz.lock.json
git -c core.editor=true rebase --continue
```

#### 4c. Workflows do upstream (deploy-v5.yaml, build-preview.yaml, ci.yaml)

Quando o erro for modify/delete para arquivos que não existem no seu repo:

```powershell
git rebase --skip
```

#### 4d. package-lock.json — manter local ou pular

```powershell
git checkout --ours package-lock.json
git add package-lock.json
git -c core.editor=true rebase --continue
# Se o commit só muda package-lock.json massivamente, pular:
# git rebase --skip
```

### 5. Push forçado

```powershell
git push --force-with-lease origin v5
```

### 6. Merge no GitHub — SEMPRE Squash and merge

Nunca usar "Create a merge commit". Usar sempre **Squash and merge** com mensagem:

```
feat: upgrade Quartz v5 - [descrição do que mudou]

- [principais mudanças do upstream]
- Mantida configuração personalizada (quartz.config.yaml)
- Mantido quartz.lock.json com plugins github: specifiers
```

## Tabela de conflitos recorrentes

| Arquivo | Tipo | Resolução |
|---|---|---|
| `quartz.config.yaml` | add/add ou modify/delete | `--ours` |
| `quartz.lock.json` | modify/delete | `--ours` |
| `package-lock.json` | content | `--ours` ou `--skip` |
| `deploy-v5.yaml` | modify/delete | `--skip` |
| `build-preview.yaml` | modify/delete | `--skip` |
| `ci.yaml` | modify/delete | `--skip` |

## Diagnóstico

```powershell
# Histórico em grafo
git log --oneline --graph --all -20

# Commits que entrarão no main
git log --oneline origin/main..v5

# Arquivos em conflito
git diff --name-only --diff-filter=U

# Detalhes de um commit problemático
git show <hash> --stat
```

## Checklist

```
[ ] git checkout v5
[ ] npx quartz upgrade
[ ] git push origin v5
[ ] Abrir PR v5 -> main no GitHub
[ ] git rebase origin/main (se houver conflitos)
[ ] Resolver conflitos (--ours nos arquivos protegidos, --skip nos do upstream)
[ ] git push --force-with-lease origin v5
[ ] PR sem conflitos no GitHub
[ ] Squash and merge com mensagem descritiva
[ ] Confirmar GitHub Actions (deploy.yml) rodou com sucesso
```

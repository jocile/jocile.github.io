# Relatório de Avisos LaTeX no Quartz

- **Total de arquivos analisados:** 874
- **Arquivos com problemas:** 2
- **Total de avisos:** 53

## Tipos de avisos

| Código | Descrição |
|--------|-----------|
| `unicodeTextInMathMode` | Caractere acentuado usado dentro de `$...$` |
| `unknownSymbol` | Caractere Unicode não reconhecido pelo KaTeX |
| `commentAtEnd` | `%` interpretado como comentário LaTeX dentro de fórmula |

## Arquivos com avisos

### 1. `content\Vagas em Sobral.md`

| Linha | Trecho | Avisos |
|------:|--------|--------|
| 18 | `1621.00 Horários 12X36 Modelo de trabalho Presencial Compartilhe Compartilhe ...` | `á` (unicodeTextInMathMode) |
| 20 | `1760.00 Horários 16:00 às 00:00 Modelo de trabalho Presencial Compartilhe Com...` | `á` (unicodeTextInMathMode), `à` (unicodeTextInMathMode), `Ç` (unicodeTextInMathMode), `Õ` (unicodeTextInMathMode) |
| 22 | `1900.00 Horários 17:00 às 01:00 Modelo de trabalho Presencial Compartilhe Com...` | `á` (unicodeTextInMathMode), `à` (unicodeTextInMathMode), `Á` (unicodeTextInMathMode) |
| 24 | `800.00 Horários Comercial Modelo de trabalho Presencial Compartilhe Compartil...` | `á` (unicodeTextInMathMode), `Ó` (unicodeTextInMathMode), `Á` (unicodeTextInMathMode) |
| 26 | `700.00 Horários Comercial Modelo de trabalho Presencial Compartilhe Compartil...` | `ã` (unicodeTextInMathMode), `á` (unicodeTextInMathMode), `ç` (unicodeTextInMathMode), `Ê` (unicodeTextInMathMode) |
| 53 | `1621.00 Horários Comercial Modelo de trabalho Presencial Compartilhe Comparti...` | `ã` (unicodeTextInMathMode), `ó` (unicodeTextInMathMode), `á` (unicodeTextInMathMode), `í` (unicodeTextInMathMode), `ç` (unicodeTextInMathMode), `ê` (unicodeTextInMathMode) |
| 91 | `1670.00 Horários 16:00 às 00:00 Modelo de trabalho Presencial Compartilhe Com...` | `ã` (unicodeTextInMathMode), `é` (unicodeTextInMathMode), `ó` (unicodeTextInMathMode), `á` (unicodeTextInMathMode), `í` (unicodeTextInMathMode), `ç` (unicodeTextInMathMode), `õ` (unicodeTextInMathMode), `ê` (unicodeTextInMathMode), `à` (unicodeTextInMathMode) |
| 129 | `800.00 Horários Comercial Modelo de trabalho Presencial Compartilhe Compartil...` | `ã` (unicodeTextInMathMode), `é` (unicodeTextInMathMode), `ó` (unicodeTextInMathMode), `á` (unicodeTextInMathMode), `í` (unicodeTextInMathMode), `ç` (unicodeTextInMathMode), `õ` (unicodeTextInMathMode), `ê` (unicodeTextInMathMode), `à` (unicodeTextInMathMode), `Á` (unicodeTextInMathMode) |
| 153 | `800.00 Horários Comercial Modelo de trabalho Presencial Compartilhe Compartil...` | `ã` (unicodeTextInMathMode), `é` (unicodeTextInMathMode), `ó` (unicodeTextInMathMode), `á` (unicodeTextInMathMode), `ç` (unicodeTextInMathMode), `õ` (unicodeTextInMathMode), `ú` (unicodeTextInMathMode), `ê` (unicodeTextInMathMode), `Ã` (unicodeTextInMathMode), `Á` (unicodeTextInMathMode), `Ç` (unicodeTextInMathMode) |

### 2. `content\private\excalidraw\Scripts\Downloaded\Mindmap Builder.md`

| Linha | Trecho | Avisos |
|------:|--------|--------|
| 1361 | `/);       if (!!parts?.[1]) {         const file = app.metadataCache.getFirst...` | `%` comentário (commentAtEnd) |
| 8482 | `{runtimeContext.t("INSTRUCTIONS")}  <div class="ex-coffee-div"><a href="https...` | `%` comentário (commentAtEnd) |

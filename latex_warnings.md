# Relatório de Avisos LaTeX no Quartz

- **Total de arquivos analisados:** 873
- **Arquivos com problemas:** 1
- **Total de avisos:** 2

## Tipos de avisos

| Código | Descrição |
|--------|-----------|
| `unicodeTextInMathMode` | Caractere acentuado usado dentro de `$...$` |
| `unknownSymbol` | Caractere Unicode não reconhecido pelo KaTeX |
| `commentAtEnd` | `%` interpretado como comentário LaTeX dentro de fórmula |

## Arquivos com avisos

### 1. `content\private\excalidraw\Scripts\Downloaded\Mindmap Builder.md`

| Linha | Trecho | Avisos |
|------:|--------|--------|
| 1361 | `/);       if (!!parts?.[1]) {         const file = app.metadataCache.getFirst...` | `%` comentário (commentAtEnd) |
| 8482 | `{runtimeContext.t("INSTRUCTIONS")}  <div class="ex-coffee-div"><a href="https...` | `%` comentário (commentAtEnd) |

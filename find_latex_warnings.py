"""
Script para encontrar arquivos Markdown que geram avisos de LaTeX no Quartz.
Busca por caracteres acentuados, símbolos Unicode e comentários '%' dentro de modo matemático ($...$ e $$...$$).
"""

import re
import os
from pathlib import Path
from collections import defaultdict

CONTENT_DIR = Path("content")
OUTPUT_FILE = Path("latex_warnings.md")

# Caracteres acentuados e especiais que geram warnings no KaTeX
ACCENTED_CHARS = {
    "ã": "ã", "é": "é", "ó": "ó", "á": "á",
    "í": "í", "ç": "ç", "õ": "õ", "ú": "ú",
    "â": "â", "ê": "ê", "ô": "ô", "à": "à",
    "ü": "ü", "Ã": "Ã", "É": "É", "Ó": "Ó",
    "Á": "Á", "Í": "Í", "Ç": "Ç", "Õ": "Õ",
    "Ú": "Ú", "Â": "Â", "Ê": "Ê", "Ô": "Ô",
    "À": "À", "Ü": "Ü",
}

SPECIAL_CHARS = {
    "\u2013": "– (en dash, U+2013)",
    "\u2014": "— (em dash, U+2014)",
    "\u2018": "' (left single quote, U+2018)",
    "\u2019": "' (right single quote, U+2019)",
    "\u201C": "\u201c (left double quote, U+201C)",
    "\u201D": "\u201d (right double quote, U+201D)",
}


def find_math_spans(text: str) -> list[tuple[int, int, str]]:
    """Encontra todas as regiões de modo matemático no texto.
    Retorna lista de (inicio, fim, trecho).
    Ignora blocos de código (``` e `).
    """
    # Primeiro, mascara blocos de código para não detectar $ dentro deles
    masked = text

    # Mascara blocos de código com ```
    masked = re.sub(r"```[\s\S]*?```", lambda m: " " * len(m.group()), masked)
    # Mascara código inline com `
    masked = re.sub(r"`[^`\n]+`", lambda m: " " * len(m.group()), masked)

    spans = []

    # $$ ... $$ (display math) — procura primeiro para não conflitar com inline
    for m in re.finditer(r"\$\$(.+?)\$\$", masked, re.DOTALL):
        spans.append((m.start(), m.end(), m.group(1)))

    # $ ... $ (inline math) — evita cifrões escapados \$
    for m in re.finditer(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)", masked, re.DOTALL):
        # Verifica se não está dentro de um span display já encontrado
        inside_display = any(s <= m.start() and m.end() <= e for s, e, _ in spans)
        if not inside_display:
            spans.append((m.start(), m.end(), m.group(1)))

    return spans


def check_file(filepath: Path) -> list[dict]:
    """Verifica um arquivo e retorna a lista de problemas encontrados."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    issues = []
    lines = text.split("\n")
    math_spans = find_math_spans(text)

    for start, end, content in math_spans:
        # Calcula o número da linha
        line_num = text[:start].count("\n") + 1

        # Trecho curto para exibição (max 80 chars)
        snippet = content.strip().replace("\n", " ")
        if len(snippet) > 80:
            snippet = snippet[:77] + "..."

        found_chars = []

        # Verifica caracteres acentuados
        for char, name in ACCENTED_CHARS.items():
            if char in content:
                found_chars.append(f"`{name}` (unicodeTextInMathMode)")

        # Verifica caracteres especiais
        for char, name in SPECIAL_CHARS.items():
            if char in content:
                found_chars.append(f"`{name}` (unknownSymbol)")

        # Verifica comentário % sem newline
        if "%" in content:
            # % que não seja \%
            if re.search(r"(?<!\\)%", content):
                found_chars.append("`%` comentário (commentAtEnd)")

        if found_chars:
            issues.append({
                "line": line_num,
                "snippet": snippet,
                "warnings": found_chars,
            })

    return issues


def main():
    if not CONTENT_DIR.exists():
        print(f"Diretório '{CONTENT_DIR}' não encontrado!")
        return

    # Coleta todos os arquivos .md
    md_files = sorted(CONTENT_DIR.rglob("*.md"))
    print(f"Analisando {len(md_files)} arquivos Markdown em '{CONTENT_DIR}/'...")

    results: dict[str, list[dict]] = {}
    total_warnings = 0

    for filepath in md_files:
        issues = check_file(filepath)
        if issues:
            rel_path = filepath.relative_to(Path("."))
            results[str(rel_path)] = issues
            total_warnings += sum(len(i["warnings"]) for i in issues)

    # Gera o relatório Markdown
    lines = []
    lines.append("# Relatório de Avisos LaTeX no Quartz\n")
    lines.append(f"- **Total de arquivos analisados:** {len(md_files)}")
    lines.append(f"- **Arquivos com problemas:** {len(results)}")
    lines.append(f"- **Total de avisos:** {total_warnings}")
    lines.append("")

    if not results:
        lines.append("> Nenhum aviso encontrado! ✅")
    else:
        lines.append("## Tipos de avisos\n")
        lines.append("| Código | Descrição |")
        lines.append("|--------|-----------|")
        lines.append("| `unicodeTextInMathMode` | Caractere acentuado usado dentro de `$...$` |")
        lines.append("| `unknownSymbol` | Caractere Unicode não reconhecido pelo KaTeX |")
        lines.append("| `commentAtEnd` | `%` interpretado como comentário LaTeX dentro de fórmula |")
        lines.append("")

        lines.append("## Arquivos com avisos\n")

        for i, (filepath, issues) in enumerate(sorted(results.items()), 1):
            lines.append(f"### {i}. `{filepath}`\n")
            lines.append("| Linha | Trecho | Avisos |")
            lines.append("|------:|--------|--------|")
            for issue in issues:
                warnings_str = ", ".join(issue["warnings"])
                snippet_escaped = issue["snippet"].replace("|", "\\|")
                lines.append(
                    f"| {issue['line']} | `{snippet_escaped}` | {warnings_str} |"
                )
            lines.append("")

    # Salva o arquivo
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nRelatório salvo em: {OUTPUT_FILE}")
    print(f"  → {len(results)} arquivo(s) com {total_warnings} aviso(s) encontrado(s).")


if __name__ == "__main__":
    main()


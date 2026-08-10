#!/usr/bin/env python3
"""
quartz-format.py — Formata notas Obsidian para publicação com Quartz v5

Uso:
    python quartz-format.py <diretório> [opções]

    # Ver o que seria feito (sem alterar nada)
    python quartz-format.py content/ --dry-run

    # Formatar todas as notas (com backup)
    python quartz-format.py content/ --backup

    # Formatar recursivamente e gerar relatório
    python quartz-format.py content/ --recursive --report relatorio.md

    # Gravar saída em outra pasta (não sobrescreve os originais)
    python quartz-format.py content/ --output content-formatado/

    # Marcar rascunhos suspeitos automaticamente
    python quartz-format.py content/ --auto-drafts --dry-run

    Opções disponíveis:

    --dry-run            # Mostra todas as mudanças sem gravar nenhum arquivo 
    --backup             # Cria cópia `.md.bak` antes de editar cada arquivo
    --recursive          # Processa subpastas recursivamente
    --auto-drafts        # Marca como `draft: true` notas suspeitas (WIP, sem parágrafos)
    --output DIR         # Grava os arquivos formatados em `DIR` em vez de sobrescrever
    --report FILE        # Salva relatório completo em Markdown no arquivo `FILE` 

"""

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("❌ Dependência ausente. Instale com: pip install pyyaml")
    sys.exit(1)


# ── Configurações ──────────────────────────────────────────────────────────────

DRAFT_PREFIXES = ("wip", "draft", "rascunho", "todo", "fixme", "xxx")
PRIVATE_TAGS   = {"private", "privado", "pessoal", "personal"}
DESC_MAX_LEN   = 160

# Tags inline Obsidian: #palavra fora de início de linha (headings)
INLINE_TAG_RE = re.compile(
    r"(?<!\n)(?<![#\w])#([a-zA-ZÀ-ÿ][a-zA-ZÀ-ÿ0-9_-]*)"
)

# Sintaxe Markdown a remover ao gerar description
MD_STRIP_RE = re.compile(
    r"\[\[([^\|\]]+)(?:\|[^\]]+)?\]\]"  # [[wikilink]] ou [[link|alias]]
    r"|\[([^\]]+)\]\([^\)]+\)"          # [texto](url)
    r"|[`*_~]+"                          # ênfase e código inline
    r"|^#+ ",                            # headings
    re.MULTILINE,
)


# ── Parser de frontmatter ──────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Retorna (frontmatter_dict, body). Body começa após o segundo '---'."""
    if not content.startswith("---"):
        return {}, content

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}, content

    try:
        fm = yaml.safe_load(match.group(1)) or {}
        if not isinstance(fm, dict):
            return {}, content
        return fm, content[match.end():]
    except yaml.YAMLError as e:
        return {"__yaml_error__": str(e)}, content


def serialize_frontmatter(fm: dict) -> str:
    """Serializa o frontmatter para YAML com bloco '---', campos em ordem preferida."""
    ordered_keys = ["title", "description", "date", "lastmod", "draft", "tags", "aliases"]
    ordered = {k: fm[k] for k in ordered_keys if k in fm}
    ordered.update({k: v for k, v in fm.items() if k not in ordered and not k.startswith("__")})

    return "---\n" + yaml.dump(
        ordered,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ) + "---\n"


# ── Extratores de conteúdo ────────────────────────────────────────────────────

def extract_title_from_h1(body: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def extract_inline_tags(body: str) -> tuple[list[str], str]:
    """
    Encontra #tags inline no corpo (fora de code blocks e headings).
    Retorna (lista_de_tags, corpo_sem_tags).
    """
    clean = strip_code_blocks(body)
    tags_found: set[str] = set()

    for m in INLINE_TAG_RE.finditer(clean):
        # Verificar se não está no início de uma linha (= heading)
        line_before = clean[clean.rfind("\n", 0, m.start()) + 1 : m.start()]
        if not line_before.strip():
            continue
        tags_found.add(m.group(1).lower())

    if not tags_found:
        return [], body

    def remove_tag(m: re.Match) -> str:
        return "" if m.group(1).lower() in tags_found else m.group(0)

    clean_body = INLINE_TAG_RE.sub(remove_tag, body)
    clean_body = re.sub(r"  +", " ", clean_body)              # colapsar espaços duplos
    clean_body = re.sub(r" +([.,;:!?])", r"\1", clean_body)   # limpar espaço antes de pontuação
    return sorted(tags_found), clean_body


def normalize_tags(tags: list) -> list[str]:
    seen: set[str] = set()
    result = []
    for tag in tags:
        t = re.sub(r"[\s_]+", "-", str(tag).lower().strip())
        t = re.sub(r"[^\w\-]", "", t)
        if t and t not in seen:
            seen.add(t)
            result.append(t)
    return sorted(result)


def generate_description(body: str, max_len: int = DESC_MAX_LEN) -> str | None:
    """Gera description a partir do primeiro parágrafo; remove sintaxe Markdown."""
    skip = re.compile(r"^(```|#{1,6} |[-*+] |\d+\. |>|\|)")
    lines: list[str] = []
    in_code = False

    for line in body.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or skip.match(line):
            continue
        if line.strip():
            lines.append(line.strip())
        elif lines:
            break  # fim do primeiro parágrafo

    if not lines:
        return None

    text = MD_STRIP_RE.sub(lambda m: m.group(1) or m.group(2) or "", " ".join(lines))
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) < 10:
        return None
    if len(text) > max_len:
        text = text[: max_len - 1].rsplit(" ", 1)[0] + "…"
    return text


def remove_duplicate_h1(body: str, title: str) -> tuple[str, bool]:
    """Remove o H1 do corpo se for textualmente idêntico ao title do frontmatter."""
    def normalize(s: str) -> str:
        return re.sub(r"[^\w\s]", "", s.lower()).strip()

    for m in re.finditer(r"^#\s+(.+)\n?", body, re.MULTILINE):
        if normalize(m.group(1)) == normalize(title):
            return (body[: m.start()] + body[m.end() :]).lstrip("\n"), True
    return body, False


def is_draft_candidate(title: str, body: str) -> str | None:
    """Retorna o motivo se a nota parece rascunho, ou None."""
    if any(title.lower().startswith(p) for p in DRAFT_PREFIXES):
        return f"título começa com prefixo de rascunho"

    stripped = strip_code_blocks(body)
    paragraphs = [
        l for l in stripped.split("\n")
        if l.strip() and not re.match(r"^(#{1,6} |[-*+] |\d+\. |>|\|)", l)
    ]
    if not paragraphs:
        return "nota sem parágrafos de texto"
    return None


# ── Processador de nota ───────────────────────────────────────────────────────

class NoteFormatter:
    def __init__(self, *, dry_run=False, backup=False, auto_drafts=False, output_dir=None):
        self.dry_run     = dry_run
        self.backup      = backup
        self.auto_drafts = auto_drafts
        self.output_dir  = Path(output_dir) if output_dir else None

    def process_file(self, path: Path) -> dict:
        result = {"changes": [], "warnings": [], "error": None, "skipped": False}

        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            result["error"] = f"Erro ao ler: {e}"
            return result

        fm, body = parse_frontmatter(content)

        if "__yaml_error__" in fm:
            result["error"] = f"YAML inválido: {fm['__yaml_error__']}"
            return result

        # 1. title
        if not fm.get("title"):
            h1 = extract_title_from_h1(body)
            if h1:
                fm["title"] = h1
                result["changes"].append(f"title extraído do H1: '{h1}'")
            else:
                fm["title"] = path.stem.replace("-", " ").replace("_", " ").title()
                result["changes"].append(f"title gerado do nome do arquivo: '{fm['title']}'")

        # 2. date
        if not fm.get("date"):
            fm["date"] = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")
            result["changes"].append(f"date adicionada (mtime): {fm['date']}")

        # 3. tags inline → frontmatter
        inline_tags, body = extract_inline_tags(body)
        if inline_tags:
            result["changes"].append(f"tags inline movidas: #{', #'.join(inline_tags)}")

        private_found = PRIVATE_TAGS & set(inline_tags)
        existing_tags = list(fm.get("tags") or [])
        all_tags = normalize_tags(existing_tags + inline_tags)

        if private_found:
            all_tags = [t for t in all_tags if t not in PRIVATE_TAGS]
            if not fm.get("draft"):
                fm["draft"] = True
                result["changes"].append(
                    f"draft: true (tag privada: #{', #'.join(private_found)})"
                )

        if all_tags:
            fm["tags"] = all_tags
            if all_tags != normalize_tags(existing_tags):
                result["changes"].append("tags normalizadas e atualizadas")

        # 4. draft
        if "draft" not in fm:
            reason = is_draft_candidate(str(fm.get("title", "")), body) if self.auto_drafts else None
            if reason:
                fm["draft"] = True
                result["changes"].append(f"draft: true (auto: {reason})")
            else:
                fm["draft"] = False
                result["changes"].append("draft: false adicionado")

            if not self.auto_drafts and is_draft_candidate(str(fm.get("title", "")), body):
                result["warnings"].append(
                    f"possível rascunho: {is_draft_candidate(str(fm.get('title','')), body)}"
                )

        # 5. description — fonte prioritária: dg-metatags.description
        if not fm.get("description"):
            dg_meta = fm.get("dg-metatags") or {}
            meta_desc = dg_meta.get("description") if isinstance(dg_meta, dict) else None

            if meta_desc:
                fm["description"] = meta_desc
                result["changes"].append("description extraída de dg-metatags.description")
            else:
                desc = generate_description(body)
                if desc:
                    fm["description"] = desc
                    result["changes"].append("description gerada do 1º parágrafo")
                else:
                    result["warnings"].append("description ausente e não foi possível gerar automaticamente")

        # 6. Limpeza de campos Obsidian/Digital Garden não usados pelo Quartz
        cleanup_keys = ["dg-note-icon", "dg-publish", "cssclasses", "dg-metatags", "topics"]
        removed_keys = [k for k in cleanup_keys if k in fm]
        for k in removed_keys:
            del fm[k]
        if removed_keys:
            result["changes"].append(f"campos removidos: {', '.join(removed_keys)}")

        # 7. H1 duplicado
        if fm.get("title"):
            body, removed = remove_duplicate_h1(body, str(fm["title"]))
            if removed:
                result["changes"].append("H1 duplicado removido do corpo")

        # 8. Avisos de wikilinks e imagens com path relativo
        n_links = len(re.findall(r"\[\[[^\]]+\]\]", body))
        if n_links:
            result["warnings"].append(
                f"{n_links} wikilink(s) detectado(s) — verificar se existem no vault"
            )

        rel_imgs = re.findall(r"!\[.*?\]\((?!https?://)(.*?)\)", body)
        if rel_imgs:
            result["warnings"].append(f"imagem(ns) com path relativo: {', '.join(rel_imgs)}")

        # Gravar
        if result["changes"] and not self.dry_run:
            new_content = serialize_frontmatter(fm) + "\n" + body

            out_path = path
            if self.output_dir:
                out_path = self.output_dir / path.name
                self.output_dir.mkdir(parents=True, exist_ok=True)

            if self.backup and out_path == path:
                shutil.copy2(path, path.with_suffix(".md.bak"))

            out_path.write_text(new_content, encoding="utf-8")

        if not result["changes"]:
            result["skipped"] = True

        return result


# ── Relatório Markdown ────────────────────────────────────────────────────────

def format_report(results: dict, dry_run: bool) -> str:
    changed = [(p, r) for p, r in results.items() if r.get("changes")]
    skipped = [(p, r) for p, r in results.items() if r.get("skipped")]
    errors  = [(p, r) for p, r in results.items() if r.get("error")]

    lines = [
        "# Relatório de Formatação Quartz",
        "",
        f"Modo: {'**dry-run** (nenhum arquivo alterado)' if dry_run else 'escrita em disco'}",
        "",
        f"**Total:** {len(results)} notas  |  "
        f"✅ {len(changed)} alteradas  |  "
        f"⏭ {len(skipped)} sem mudanças  |  "
        f"❌ {len(errors)} com erro",
        "",
    ]

    if errors:
        lines += ["## ❌ Erros", ""]
        for path, r in errors:
            lines.append(f"- `{path}`: {r['error']}")
        lines.append("")

    if changed:
        lines += ["## ✅ Notas alteradas", ""]
        for path, r in changed:
            lines.append(f"### `{path}`")
            for c in r["changes"]:
                lines.append(f"- ✅ {c}")
            for w in r.get("warnings", []):
                lines.append(f"- ⚠️  {w}")
            lines.append("")

    if skipped:
        lines += ["## ⏭ Sem mudanças necessárias", ""]
        for path, _ in skipped:
            lines.append(f"- `{path}`")
        lines.append("")

    return "\n".join(lines)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Formata notas Obsidian para publicação com Quartz v5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python quartz-format.py content/ --dry-run
  python quartz-format.py content/ --backup --recursive --report relatorio.md
  python quartz-format.py content/ --output content-formatado/
  python quartz-format.py content/ --auto-drafts
        """,
    )
    parser.add_argument("directory",     help="Diretório com as notas .md")
    parser.add_argument("--dry-run",     action="store_true", help="Mostrar mudanças sem gravar")
    parser.add_argument("--backup",      action="store_true", help="Criar .md.bak antes de editar")
    parser.add_argument("--recursive",   action="store_true", help="Processar subpastas")
    parser.add_argument("--auto-drafts", action="store_true", help="Marcar rascunhos suspeitos como draft: true")
    parser.add_argument("--output",      metavar="DIR",       help="Gravar saída em outro diretório")
    parser.add_argument("--report",      metavar="FILE",      help="Salvar relatório Markdown em FILE")
    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.is_dir():
        print(f"❌ Diretório não encontrado: {directory}")
        sys.exit(1)

    formatter = NoteFormatter(
        dry_run=args.dry_run,
        backup=args.backup,
        auto_drafts=args.auto_drafts,
        output_dir=args.output,
    )

    files = sorted(directory.glob("**/*.md" if args.recursive else "*.md"))
    if not files:
        print(f"Nenhum arquivo .md encontrado em {directory}")
        sys.exit(0)

    print(f"\n🔍 Processando {len(files)} nota(s){'  [DRY RUN]' if args.dry_run else ''}...\n")

    all_results: dict[str, dict] = {}
    for path in files:
        rel = str(path.relative_to(directory))
        r = formatter.process_file(path)
        all_results[rel] = r

        if r.get("error"):
            print(f"  ❌ {rel}: {r['error']}")
        elif r.get("skipped"):
            print(f"  ⏭  {rel}: ok")
        else:
            print(f"  ✅ {rel}: {len(r['changes'])} mudança(s)")
            for c in r["changes"]:
                print(f"      · {c}")
            for w in r.get("warnings", []):
                print(f"      ⚠  {w}")

    n_changed = sum(1 for r in all_results.values() if r.get("changes"))
    n_skip    = sum(1 for r in all_results.values() if r.get("skipped"))
    n_err     = sum(1 for r in all_results.values() if r.get("error"))

    print(f"\n{'─' * 55}")
    print(f"Total: {len(files)}  |  ✅ {n_changed} alteradas  |  ⏭ {n_skip} ok  |  ❌ {n_err} erros")
    if args.dry_run:
        print("⚠️  Modo dry-run: nenhum arquivo foi modificado.")

    if args.report:
        report_path = Path(args.report)
        report_path.write_text(format_report(all_results, args.dry_run), encoding="utf-8")
        print(f"📄 Relatório salvo em: {report_path}")


if __name__ == "__main__":
    main()

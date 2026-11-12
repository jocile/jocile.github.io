"""
Script para corrigir avisos de LaTeX no Quartz.
Escapa o símbolo $ usado como moeda (R$ e $) fora de blocos de código.
"""

import re
from pathlib import Path

# Arquivos que NÃO devem ser modificados (auto-gerados / scripts)
SKIP_FILES = {
    Path(r"content\private\excalidraw\Scripts\Downloaded\Mindmap Builder.md"),
}

# Todos os arquivos problemáticos do relatório
TARGET_FILES = [
    Path(r"content\cursos_senac_sobral.md"),
    Path(r"content\gemini-scribe\Agent-Sessions\2026-10-12 Python, SQL & Bottle for Web Apps.md"),
    Path(r"content\gemini-scribe\Agent-Sessions\2026-11-08 Python e TDD- Fundamentos e Desafios.md"),
    Path(r"content\notas\Python\Atividades\sistema bancario\Desafio conta bancaria 2.md"),
    Path(r"content\notas\Python\Atividades\sistema bancario\Desafio sistema bancario.md"),
    Path(r"content\notas\Python\Condicionais com Python.md"),
    Path(r"content\notas\Python\Introducao ao SQL e Bottle para construir Apps em Python.md"),
    Path(r"content\notas\UX design\Briefing.md"),
    Path(r"content\private\Desafios-de-Codigo\Desafio telefone.md"),
    Path(r"content\private\Desafios-de-Codigo\Desafios Python\Saldo de Transacoes Bancarias.md"),
    Path(r"content\private\Python\Condicionais-em-python.md"),
    Path(r"content\private\Python\Desafio-bancario-fluxograma antigo.md"),
    Path(r"content\private\Python\Exercícios condicionais com Python.md"),
    Path(r"content\turmas\programador de sistema\UC2 - Programador de Sistemas\Pratica Pandas\Atividade Analista de Dados Educacionais.md"),
    Path(r"content\turmas\programador de sistema\UC2 - Programador de Sistemas\Pratica Pandas\Gabarito Atividade Analista de Dados Educacionais.md"),
    Path(r"content\turmas\programador de sistema\UC2 - Programador de Sistemas\Pratica Pandas\atividade_pandas sqlite.md"),
    Path(r"content\turmas\programador de sistema\UC2 - Programador de Sistemas\Pratica produtos\produtos-01-crud-analise.md"),
    Path(r"content\turmas\programador de sistema\UC2 - Programador de Sistemas\Pratica produtos\produtos-02-vendas-estoque.md"),
    Path(r"content\turmas\programador de sistema\UC2 - Programador de Sistemas\Pratica produtos\produtos-03-visualizacao.md"),
    Path(r"content\turmas\programador de sistema\UC3 - Programador de Sistemas\uc3.05 - Analisando resultados e medindo cobertura.md"),
]


def escape_dollar_in_segment(segment: str) -> tuple[str, int]:
    """
    Escapa $ usado como moeda em um segmento de texto puro (fora de código).
    Retorna (texto_corrigido, numero_de_alteracoes).
    """
    result = []
    changes = 0
    i = 0

    while i < len(segment):
        # Caso 1: R$ (Real brasileiro) — não já escapado
        if (segment[i] == 'R' and i + 1 < len(segment) and segment[i + 1] == '$'):
            result.append('R\\$')
            changes += 1
            i += 2
            continue

        # Caso 2: \$ (já escapado) — manter como está
        if segment[i] == '\\' and i + 1 < len(segment) and segment[i + 1] == '$':
            result.append('\\$')
            i += 2
            continue

        # Caso 3: $ seguido de dígito (ex: $4, $0.10) — moeda dólar
        if (segment[i] == '$' and i + 1 < len(segment) and segment[i + 1].isdigit()):
            result.append('\\$')
            changes += 1
            i += 1
            continue

        # Caso 4: $ seguido de espaço e dígito (ex: "pagar $ 1.000") - raro mas possível
        # Não escapar pois pode ser algo legítimo

        # Caso 5: $$ (display math LaTeX) — manter
        if segment[i] == '$' and i + 1 < len(segment) and segment[i + 1] == '$':
            result.append('$$')
            i += 2
            continue

        result.append(segment[i])
        i += 1

    return ''.join(result), changes


def fix_line(line: str) -> tuple[str, int]:
    """
    Corrige uma única linha, preservando código inline e fórmulas LaTeX legítimas.
    Retorna (linha_corrigida, numero_de_alteracoes).
    """
    # Se a linha é uma fórmula LaTeX legítima ($$...\command...), pular
    if re.search(r'^\s*\$\$.*\\(text|frac|times|sqrt|sum|int|cdot)', line):
        return line, 0

    # Divide a linha em partes: código inline vs texto normal
    # Regex: captura `...` como grupo, o resto é texto normal
    parts = re.split(r'(`[^`]*`)', line)
    total_changes = 0
    fixed_parts = []

    for part in parts:
        if part.startswith('`') and part.endswith('`') and len(part) >= 2:
            # Código inline — não modificar
            fixed_parts.append(part)
        else:
            fixed, changes = escape_dollar_in_segment(part)
            fixed_parts.append(fixed)
            total_changes += changes

    return ''.join(fixed_parts), total_changes


def fix_file(text: str) -> tuple[str, int]:
    """
    Corrige todo o texto de um arquivo.
    Retorna (texto_corrigido, numero_total_de_alteracoes).
    """
    lines = text.split('\n')
    result = []
    total_changes = 0
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        # Detecta início/fim de bloco de código cercado (```)
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            # Dentro de bloco de código — não modificar
            result.append(line)
            continue

        # Fora de bloco de código — aplicar correções
        fixed_line, changes = fix_line(line)
        result.append(fixed_line)
        total_changes += changes

    return '\n'.join(result), total_changes


def main():
    print("=" * 60)
    print("  Correção de avisos LaTeX — Escapando $ como moeda")
    print("=" * 60)
    print()

    total_files_fixed = 0
    total_changes = 0
    skipped = []
    not_found = []
    no_changes = []
    fixed = []

    for filepath in TARGET_FILES:
        if filepath in SKIP_FILES:
            skipped.append(str(filepath))
            continue

        if not filepath.exists():
            not_found.append(str(filepath))
            continue

        try:
            original = filepath.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  ❌ Erro lendo {filepath}: {e}")
            continue

        fixed_text, changes = fix_file(original)

        if changes == 0:
            no_changes.append(str(filepath))
            continue

        # Salvar arquivo corrigido
        filepath.write_text(fixed_text, encoding='utf-8')
        total_files_fixed += 1
        total_changes += changes
        fixed.append((str(filepath), changes))
        print(f"  ✅ {filepath} — {changes} correções")

    print()

    if skipped:
        print("Arquivos pulados (auto-gerados/scripts):")
        for f in skipped:
            print(f"  ⏭ {f}")
        print()

    if not_found:
        print("Arquivos não encontrados:")
        for f in not_found:
            print(f"  ⚠ {f}")
        print()

    if no_changes:
        print("Arquivos sem alterações necessárias:")
        for f in no_changes:
            print(f"  ⏭ {f}")
        print()

    print("=" * 60)
    print(f"  Resumo: {total_files_fixed} arquivos corrigidos, {total_changes} alterações")
    print("=" * 60)
    print()
    print("Execute 'python find_latex_warnings.py' para verificar os avisos restantes.")


if __name__ == "__main__":
    main()

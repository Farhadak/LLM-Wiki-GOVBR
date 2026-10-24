#!/usr/bin/env python3
"""Prepara cópias Markdown do Obsidian para o MkDocs."""

from pathlib import Path
import json
import os
import re

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "scripts/publication-manifest.json"
OUTPUT = ROOT / "docs-public"
WIKILINK = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")


def load_manifest():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert data["publication_status"] == "preparacao_beta"
    assert data["review_human"] == "pendente"
    assert data["review_legal"] == "pendente"

    pages = [Path(name) for name in data["pages"]]
    assert len(pages) == len(set(pages))

    for page in pages:
        assert not page.is_absolute()
        assert ".." not in page.parts
        assert page.suffix == ".md"
        assert (ROOT / page).is_file(), f"Arquivo ausente: {page}"

    return data, pages


def build_index(pages):
    index = {}

    for page in pages:
        if page.stem in index:
            raise ValueError(f"Nome ambíguo: {page.stem}")

        index[page.stem] = page

    return index


def convert_links(text, source, index, exceptions):
    def replace(match):
        raw = match.group(1)
        target, separator, alias = raw.partition("|")
        target = target.strip()
        label = alias.strip() if separator else target

        if target in index:
            destination = index[target]
            relative = os.path.relpath(
                destination,
                start=source.parent
            )
            return f"[{label}]({Path(relative).as_posix()})"

        if target in exceptions:
            return f"{label} ({exceptions[target]})"

        raise ValueError(
            f"Link sem destino autorizado em {source}: {raw}"
        )

    return WIKILINK.sub(replace, text)




def add_publication_notice(content, notice):
    """Insere o aviso após o frontmatter YAML, quando presente."""
    if content.startswith("---\n"):
        closing = content.find("\n---\n", 4)
        if closing == -1:
            raise ValueError("Frontmatter YAML sem fechamento")

        position = closing + len("\n---\n")
        return (
            content[:position]
            + "\n"
            + notice
            + "\n\n"
            + content[position:]
        )

    return notice + "\n\n" + content


def main():
    manifest, pages = load_manifest()
    index = build_index(pages)
    exceptions = manifest["excluded_links"]
    notice = (ROOT / "scripts/PUBLICATION-NOTICE.md").read_text(
        encoding="utf-8"
    ).strip()

    converted = {}

    for source in pages:
        original = (ROOT / source).read_text(encoding="utf-8")
        converted[source] = add_publication_notice(
            convert_links(original, source, index, exceptions),
            notice
        )

    # Página inicial pública, com links relativos à raiz.
    home_source = Path("00-Inicio/INDEX.md")
    assert home_source in converted

    home_original = (ROOT / home_source).read_text(encoding="utf-8")
    home_public = add_publication_notice(
        convert_links(
            home_original,
            Path("index.md"),
            index,
            exceptions
        ),
        notice
    )

    # Só escreve depois de validar todas as páginas.
    OUTPUT.mkdir(exist_ok=True)

    for source, content in converted.items():
        destination = OUTPUT / source
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")

    (OUTPUT / "index.md").write_text(
        home_public, encoding="utf-8"
    )

    print(f"Páginas geradas: {len(converted) + 1}")
    print(f"Destino: {OUTPUT}")
    print("Revisão humana: pendente")
    print("Revisão jurídica: pendente")


if __name__ == "__main__":
    main()

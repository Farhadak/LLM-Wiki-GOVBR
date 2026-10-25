#!/usr/bin/env python3
"""Gera dados do grafo a partir das páginas autorizadas."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "scripts/publication-manifest.json"
OUTPUT = ROOT / "docs-public/assets/knowledge-graph.json"

WIKILINK = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = [Path(name) for name in manifest["pages"]]

    assert len(pages) == len(set(pages))

    index = {}
    for page in pages:
        assert not page.is_absolute()
        assert ".." not in page.parts
        assert page.suffix == ".md"
        assert (ROOT / page).is_file()

        if page.stem in index:
            raise ValueError(f"Nome ambíguo: {page.stem}")

        index[page.stem] = page

    nodes = []
    edges = set()

    for page in pages:
        content = (ROOT / page).read_text(encoding="utf-8")

        title_match = re.search(
            r"^title:\s*(.+)$",
            content,
            flags=re.MULTILINE,
        )

        title = (
            title_match.group(1).strip().strip("\"'")
            if title_match
            else page.stem
        )

        nodes.append({
            "id": page.as_posix(),
            "label": title,
            "category": page.parts[0],
            "url": page.with_suffix("").as_posix() + "/",
        })

        for match in WIKILINK.finditer(content):
            raw = match.group(1)
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()

            if target not in index:
                continue

            destination = index[target].as_posix()
            source = page.as_posix()

            if source != destination:
                edges.add(tuple(sorted((source, destination))))

    data = {
        "nodes": nodes,
        "edges": [
            {"source": source, "target": target}
            for source, target in sorted(edges)
        ],
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("NÓS:", len(nodes))
    print("RELAÇÕES:", len(edges))
    print("ARQUIVO:", OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()

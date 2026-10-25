#!/usr/bin/env python3
"""Constrói os componentes públicos do grafo de conhecimento."""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
ASSETS = SCRIPTS / "graph-assets"
DESTINATION = ROOT / "docs-public/assets"

def run(script):
    subprocess.run(
        [sys.executable, str(SCRIPTS / script)],
        cwd=ROOT,
        check=True,
    )

def main():
    run("build_graph.py")
    run("build_graph_view.py")

    DESTINATION.mkdir(parents=True, exist_ok=True)

    for filename in (
        "knowledge-graph.js",
        "knowledge-graph.css",
    ):
        source = ASSETS / filename

        if not source.is_file():
            raise FileNotFoundError(source)

        target = DESTINATION / filename
        shutil.copy2(source, target)

        print("RECURSO INTEGRADO:", target.relative_to(ROOT))

    required = [
        ROOT / "docs-public/Grafo-de-Conhecimento.md",
        DESTINATION / "knowledge-graph.json",
        DESTINATION / "knowledge-graph.js",
        DESTINATION / "knowledge-graph.css",
    ]

    missing = [path for path in required if not path.is_file()]

    if missing:
        for path in missing:
            print("AUSENTE:", path.relative_to(ROOT))
        sys.exit(1)

    print("ARQUIVOS DO GRAFO:", len(required))
    print("RESULTADO: APROVADO")

if __name__ == "__main__":
    main()

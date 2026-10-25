#!/usr/bin/env python3
"""Gera a página de visualização do grafo para o MkDocs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs-public/Grafo-de-Conhecimento.md"

PAGE = r'''# Grafo de Conhecimento

!!! warning "Publicação beta — revisão pendente"
    Esta é uma publicação editorial independente, não oficial do Governo Federal. As revisões humana e jurídica permanecem pendentes. Consulte as fontes primárias antes de utilizar seu conteúdo como referência normativa.

Explore as conexões documentadas entre os conceitos da Wiki. As relações representam referências explícitas entre páginas, não relações causais ou equivalências semânticas verificadas.

<div class="graph-controls">
  <input id="graph-search" type="search" placeholder="Pesquisar conceito..." aria-label="Pesquisar conceito">
  <select id="graph-category" aria-label="Filtrar domínio">
    <option value="">Todos os domínios</option>
  </select>
  <button id="graph-reset" type="button">Restaurar visualização</button>
</div>

<div id="knowledge-graph" role="img" aria-label="Grafo interativo de conceitos da Wiki"></div>
<p id="graph-status" role="status">Carregando grafo...</p>
<p><small>Arraste os nós para reorganizá-los. Use a roda do mouse para ampliar ou reduzir. Clique duas vezes em um nó para abrir sua página.</small></p>

<link rel="stylesheet" href="../assets/knowledge-graph.css">
<script defer src="https://cdn.jsdelivr.net/npm/cytoscape@3.30.4/dist/cytoscape.min.js"></script>
<script defer src="../assets/knowledge-graph.js"></script>
'''

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(PAGE, encoding="utf-8")

print("PÁGINA CRIADA:", OUTPUT.relative_to(ROOT))

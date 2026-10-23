---
title: Geração Aumentada via Recuperação
aliases:
  - RAG
  - Retrieval-Augmented Generation
type: conceito
status: rascunho
source_id: FONTE-001
review_status: pendente
review_human: pendente
review_legal: pendente
---

# Geração Aumentada via Recuperação (RAG)

[[Fundamentos|Voltar a Fundamentos]]

## 1. Conteúdo oficial — síntese atribuída à fonte

O guia da Secretaria de Governo Digital (SGD) e do
SERPRO apresenta a Geração Aumentada via Recuperação
(RAG, Retrieval-Augmented Generation) como uma técnica
que combina geração de texto e recuperação de informações.

Segundo o documento, RAG permite complementar um
modelo de inteligência artificial generativa com
informações provenientes de uma base de conhecimento.

O guia destaca sua aplicação na gestão do conhecimento
e na utilização de dados institucionais.

**Referência:** [[guia-ia-generativa-normalizado]],
linhas 74–78.

## 2. Distinção entre RAG e ajuste do modelo

Conforme o guia, a abordagem RAG combina o modelo
com sistemas capazes de consultar bases de informação,
sem exigir o ajuste direto do modelo.

O documento também apresenta o fine-tuning como
possibilidade de adaptação de modelos abertos.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 68–78.

## 3. Análise técnica — elaboração editorial

Em uma arquitetura RAG, um sistema pode recuperar
documentos ou trechos relevantes e disponibilizá-los
como contexto para a geração de uma resposta.

A qualidade depende, entre outros fatores, da
pertinência dos documentos recuperados, da qualidade
das fontes e da capacidade de utilizar corretamente
as informações disponibilizadas.

RAG não garante ausência de alucinações, correção
factual ou fidelidade automática aos documentos.

RAG e fine-tuning são abordagens distintas, mas
podem ser utilizadas de maneira complementar.

Essas observações são análise editorial e não
constituem afirmações atribuídas ao guia oficial.

## 4. Implicações para governança — proposta editorial

Uma implementação institucional de RAG deve considerar:

- Identificação e proveniência das fontes documentais.
- Controle de acesso às informações recuperadas.
- Gestão de versões e atualização das bases consultadas.
- Verificação da correspondência entre resposta e fonte.
- Registro de limitações e incertezas das respostas.
- Avaliação da qualidade da recuperação e da geração.
- Supervisão humana proporcional aos riscos de uso.

Esses requisitos são propostas editoriais que
dependem de fundamentação técnica complementar
e validação humana.

## 5. Aplicação potencial à Wiki GOV.BR

A Wiki poderá servir como base documental para
um sistema de recuperação de informações, desde
que sejam preservadas as distinções entre:

- Conteúdo oficial e sua proveniência.
- Normalização editorial dos documentos.
- Análises críticas produzidas para a Wiki.
- Recomendações de governança ainda não validadas.

A utilização de RAG constitui uma possibilidade
arquitetural futura, não uma funcionalidade já
implementada neste repositório.

## 6. Rastreabilidade

- Fonte cadastrada: [[FONTE-001]]
- Documento: [[guia-ia-generativa-normalizado]]
- Modelos abertos e ajuste: linhas 68–72
- Definição e aplicação de RAG: linhas 74–78
- Cadeia documental: [[PROVENIENCIA]]
- Conceito relacionado: [[Grandes Modelos de Linguagem]]
- Natureza: síntese e análise editorial
- Revisão humana: pendente

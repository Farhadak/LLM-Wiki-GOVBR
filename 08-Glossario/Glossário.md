---
title: Glossário
type: glossario
status: rascunho
source_id: FONTE-001
created: 2026-10-22
review_human: pendente
review_legal: pendente
verification_external: pendente
---

# Glossário — Inteligência Artificial Generativa no Setor Público

## 1. Objetivo e critérios editoriais

Este glossário reúne conceitos técnicos e institucionais relevantes para a compreensão e a utilização responsável da inteligência artificial generativa (IAG) na administração pública.

A principal referência documental é o [[guia-ia-generativa-normalizado]], identificado na Wiki como [[FONTE-001]].

As definições são classificadas em três categorias:

- **Definição presente no guia:** o documento explica expressamente o conceito.
- **Conceito mencionado no guia:** o termo aparece, mas sua definição exige complementação.
- **Complementação editorial:** explicação formulada para facilitar a compreensão, sem atribuição indevida ao documento oficial.

As explicações são paráfrases, não transcrições literais. As linhas indicadas correspondem à versão normalizada preservada nesta Wiki.

## 2. Conceitos fundamentais

### Alucinação

**Categoria:** definição presente no guia.

Produção de conteúdo aparentemente convincente, mas que pode conter erros factuais ou informações sem sustentação adequada.

O fenômeno exige conferência das respostas com fontes confiáveis, sobretudo quando seu conteúdo possa influenciar decisões administrativas.

**Fonte:** guia, linhas 23–26.

**Conexão:** [[Alucinações na IA Generativa]].

### Deepfake

**Categoria:** conceito mencionado no guia, com complementação editorial.

Conteúdo sintético de imagem, áudio ou vídeo que pode simular de maneira convincente a aparência, a voz ou as ações de pessoas.

O guia destaca seu possível emprego em fraudes e a necessidade de cautela na produção de conteúdos multimídia.

**Fonte:** guia, linhas 134 e 380.

**Conexão:** [[Riscos]].

### Inteligência Artificial Analítica ou Preditiva

**Categoria:** definição presente no guia.

Abordagem de IA orientada ao processamento de dados existentes para produzir previsões, recomendações ou classificações e apoiar a tomada de decisão.

Distingue-se da IA generativa pelo foco principal na análise e inferência, em vez da criação de conteúdo sintético.

**Fonte:** guia, linha 30.

**Conexão:** [[Inteligência Artificial Generativa]].

### Inteligência Artificial Generativa (IAG)

**Categoria:** definição presente no guia.

Ramo da inteligência artificial voltado à produção de conteúdos, como textos, imagens, áudios, vídeos e códigos, a partir de padrões aprendidos durante o treinamento de modelos computacionais.

A capacidade de gerar conteúdo não garante precisão factual, adequação contextual ou conformidade institucional.

**Fonte:** guia, linhas 21, 24, 30 e 34.

**Conexão:** [[Inteligência Artificial Generativa]].

### Large Language Model (LLM)

**Categoria:** definição presente no guia.

Grande modelo de linguagem treinado para identificar padrões linguísticos e gerar sequências de texto em resposta a entradas do usuário.

O guia descreve seu funcionamento probabilístico e ressalta que a fluência textual não garante confiabilidade.

**Fonte:** guia, linhas 21–24.

**Conexão:** [[Grandes Modelos de Linguagem]].

### Prompt

**Categoria:** definição presente no guia.

Entrada ou instrução fornecida pelo usuário a um modelo de IA generativa para orientar a geração de uma resposta.

A clareza da instrução pode contribuir para a adequação do resultado, mas não elimina a necessidade de revisão humana.

**Fonte:** guia, linhas 23, 277 e 315.

**Conexão:** [[Boas Práticas]].
## 3. Modelos, técnicas e tratamento de dados

### Fine-tuning (ajuste fino)

**Categoria:** conceito mencionado no guia, com complementação editorial.

Processo de adaptação de um modelo previamente treinado mediante treinamento adicional com dados selecionados para determinada finalidade.

Diferentemente do RAG, o ajuste fino modifica parâmetros do modelo. Sua adoção requer avaliação da qualidade dos dados, dos custos e dos riscos associados.

**Fonte:** guia, linha 72.

**Conexão:** [[Grandes Modelos de Linguagem]].

### Geração Aumentada via Recuperação (RAG)

**Categoria:** definição presente no guia.

Técnica que combina a geração de respostas por modelos de linguagem com a recuperação de informações provenientes de bases de conhecimento.

O guia esclarece que o RAG permite consultar informações institucionais sem necessariamente modificar os parâmetros do modelo.

A recuperação de documentos não elimina riscos de respostas incorretas ou de uso de fontes desatualizadas.

**Fonte:** guia, linhas 74–78.

**Conexão:** [[Geração Aumentada via Recuperação]].

### Modelo de IA de Finalidade Geral

**Categoria:** conceito explicado no guia.

Modelo de inteligência artificial que pode ser empregado em diferentes tarefas, em vez de se restringir a uma única aplicação previamente definida.

O guia apresenta grandes modelos generativos como exemplos dessa categoria.

**Fonte:** guia, linha 32.

**Conexão:** [[Inteligência Artificial Generativa]].

### Modelos abertos e fechados

**Categoria:** distinção apresentada no guia, com complementação editorial.

Categorias utilizadas para discutir as condições de acesso, licenciamento, execução e adaptação de modelos de inteligência artificial.

A classificação exige a análise das condições específicas de cada modelo. A disponibilidade de seus pesos não significa, por si só, que o código, os dados de treinamento ou todas as permissões de uso sejam abertos.

A execução local pode ampliar o controle institucional, mas não garante, por si só, segurança ou conformidade.

**Fonte:** guia, linhas 42–72.

**Conexão:** [[Critérios de Escolha de Ferramentas]].

### Tokenização para proteção de dados

**Categoria:** conceito mencionado no guia, com complementação editorial.

Técnica que substitui determinados valores de dados por identificadores ou representações alternativas, de acordo com um mecanismo de correspondência e proteção.

Nesse contexto, não deve ser confundida com a divisão de textos em unidades de processamento utilizada em modelos de linguagem.

A tokenização não equivale necessariamente à anonimização irreversível, nem afasta automaticamente a aplicação da LGPD.

**Fonte:** guia, linhas 138–140.

**Conexão:** [[LGPD e Proteção de Dados na IA Generativa]].

## 4. Riscos e qualidade dos resultados

Viés algorítmico

Categoria: definição presente no guia.

Distorção introduzida por decisões de projeto do algoritmo, como ponderações, critérios de otimização ou priorização de determinados resultados.

Fonte: guia, linha 158.

Conexão: [[Vieses na IA Generativa]].

Viés de automação

Categoria: definição presente no guia.

Tendência humana de confiar excessivamente em resultados ou recomendações automatizadas, mesmo quando podem estar incorretos.

É particularmente relevante quando respostas de IA são utilizadas para apoiar decisões administrativas.

Fonte: guia, linha 148.

Conexões: [[Vieses na IA Generativa]]; [[Supervisão Humana e Responsabilidade]].

Vieses nos dados e na interação

Categoria: conceitos explicados no guia.

Distorções relacionadas à representatividade, à seleção, à exclusão de grupos, a desigualdades históricas ou a interações que reforçam padrões inadequados.

O guia distingue diferentes mecanismos de formação e reprodução de vieses, que exigem avaliações específicas.

Fonte: guia, linhas 142–160.

Conexão: [[Vieses na IA Generativa]].

## 5. Governança e responsabilidade institucional

### Dados pessoais e dados pessoais sensíveis

**Categoria:** conceitos mencionados no guia, com complementação jurídica editorial.

Dados pessoais são informações relacionadas a pessoas naturais identificadas ou identificáveis.

Dados pessoais sensíveis constituem uma categoria específica prevista na Lei Geral de Proteção de Dados (LGPD), sujeita a requisitos próprios de tratamento.

A utilização de IA generativa exige avaliar a finalidade do tratamento, a necessidade dos dados, as condições de acesso e as medidas de proteção aplicáveis.

**Fonte:** guia, linhas 250, 446 e 486.

**Referência jurídica a conferir:** Lei nº 13.709/2018, especialmente artigo 5º.

**Conexão:** [[LGPD e Proteção de Dados na IA Generativa]].

### Governança de IA generativa

**Categoria:** complementação editorial baseada nos princípios e nas orientações do guia.

Conjunto de responsabilidades, processos, critérios e controles utilizados para orientar a seleção, a implantação, a operação e a avaliação de sistemas de IA generativa.

Abrange a definição de finalidades, a gestão de riscos, a supervisão humana, a transparência, a proteção de dados e a avaliação dos resultados institucionais.

**Fonte:** síntese editorial dos princípios e orientações do guia, especialmente linhas 80–90, 124–126 e 273–285.

**Conexão:** [[Governança]].

### Lei Geral de Proteção de Dados (LGPD)

**Categoria:** legislação mencionada no guia, com complementação jurídica editorial.

Lei nº 13.709/2018, que disciplina o tratamento de dados pessoais, inclusive em meios digitais, observadas suas disposições e hipóteses de aplicação.

A utilização de IA generativa não dispensa o cumprimento das obrigações legais aplicáveis ao tratamento de dados.

**Fonte:** guia, linhas 82, 122 e 486.

**Referência jurídica:** Lei nº 13.709/2018. A interpretação de obrigações específicas requer consulta à legislação vigente e, quando necessário, à assessoria jurídica competente.

**Conexão:** [[LGPD e Proteção de Dados na IA Generativa]].

### Responsabilidade humana

**Categoria:** princípio explicado no guia.

Dever de revisar, validar e assumir a responsabilidade institucional pelos conteúdos e pelas decisões produzidos com apoio de IA generativa, conforme as atribuições de cada agente público.

O guia ressalta que a automação não elimina a responsabilidade do servidor pela produção e pelo uso do conteúdo.

**Fonte:** guia, linhas 26 e 126.

**Conexão:** [[Supervisão Humana e Responsabilidade]].

### Supervisão humana

**Categoria:** princípio explicado no guia, com complementação editorial.

Participação efetiva de pessoas competentes na avaliação dos resultados e no controle do uso institucional de sistemas de IA.

Pode envolver a revisão de conteúdos, a identificação de erros, a avaliação de riscos e a intervenção antes de decisões com consequências relevantes.

**Fonte:** guia, linhas 26, 40 e 182.

**Conexão:** [[Supervisão Humana e Responsabilidade]].

### Transparência e auditabilidade

**Categoria:** princípios presentes no guia, com complementação editorial.

Transparência refere-se à disponibilização de informações pertinentes sobre o uso e as condições de funcionamento da IA, respeitados os limites legais.

Auditabilidade é a possibilidade de examinar processos, registros, critérios e evidências para avaliar o funcionamento e os resultados de um sistema.

O guia associa a transparência à possibilidade de auditoria e contestação.

**Fonte:** guia, linhas 86–88 e 182.

**Conexão:** [[Transparência e Auditabilidade da IA Generativa]].

## 6. Rastreabilidade e limites do glossário

**Fonte documental principal:** [[FONTE-001]].

**Documento consultado:** [[guia-ia-generativa-normalizado]].

**Natureza das definições:** paráfrases do guia e complementações editoriais identificadas individualmente.

**Hierarquia das fontes:** o guia constitui uma referência orientativa; não substitui leis, regulamentos ou atos oficiais aplicáveis.

**Verificação jurídica externa:** pendente para definições e interpretações que dependam de legislação vigente.

**Revisão humana:** pendente.

**Revisão jurídica:** pendente.

Este glossário é um instrumento de consulta e navegação da Wiki. Não constitui parecer técnico ou jurídico, nem substitui a verificação das fontes originais.


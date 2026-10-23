---
title: Credenciais e Informações Protegidas
aliases:
  - Proteção de Credenciais e Dados no Uso de IAG
type: boa-pratica
status: rascunho
source_id: FONTE-001
review_status: pendente
---

# Credenciais e Informações Protegidas

## 1. Objetivo e delimitação

Esta nota reúne orientações práticas de prevenção
à exposição de credenciais, dados pessoais,
informações institucionais protegidas e conteúdos
sujeitos a direitos de propriedade intelectual
durante o uso de inteligência artificial generativa
(IAG) na administração pública.

O foco é a conduta operacional antes e durante
a interação com ferramentas de IAG.

As políticas de autorização, classificação,
segurança e governança dos dados são tratadas
em [[Governança e Proteção de Dados na IA Generativa]].
O alinhamento ao código de conduta institucional
é tratado em [[Conduta Institucional e Responsabilidade]].

## 2. Conteúdo oficial — síntese atribuída à fonte

### Informações sensíveis e sigilosas

O guia orienta cautela no compartilhamento
de informações sensíveis, dados pessoais
e decisões oficiais de caráter sigiloso.

Também recomenda considerar como as perguntas
enviadas às ferramentas poderão ser utilizadas
e buscar orientação especializada quando houver
dúvidas sobre privacidade e segurança.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 250–259 e 267.

### Credenciais e identificação institucional

O guia recomenda evitar o uso de e-mails,
números de telefone e credenciais institucionais
na criação de contas em plataformas externas
de IAG sem aprovação apropriada.

A preocupação inclui a associação indevida
entre o uso individual e identidade institucional.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 344–351 e 450.

### Informações internas e dados pessoais

O guia recomenda não inserir informações
internas ou protegidas em ferramentas
não aprovadas pelo órgão.

Os exemplos incluem dados de contratos,
projetos em andamento, políticas internas
e informações pessoais de servidores,
cidadãos ou terceiros.

O documento apresenta o uso de informações
fictícias ou simuladas como alternativa
para determinados testes.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 353–365 e 448.

### Soluções aprovadas e plataformas externas

O guia prioriza ferramentas internas
ou institucionalmente aprovadas e associa
sua seleção à confidencialidade,
ao controle e à auditabilidade.

Para ferramentas externas, recomenda consultar
as políticas de segurança e avaliar
o tratamento posterior das informações,
inclusive eventual uso para treinamento.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 261, 420–432.

### Anonimização e agregação de informações

O guia recomenda evitar o fornecimento
de dados pessoais e pessoais sensíveis
a ferramentas de IAG, indicando anonimização
quando o tratamento for inevitável.

Também alerta para a possibilidade de inferir
informações confidenciais a partir
da agregação de conteúdos enviados
em diferentes interações.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 444–452.

**Ressalva sobre anonimização — REV-002:** as técnicas mencionadas pelo guia, como mascaramento, tokenização, generalização e substituição por dados sintéticos, não garantem, isoladamente, anonimização juridicamente efetiva nos termos da LGPD.

A avaliação deve considerar a possibilidade de reidentificação, os meios técnicos razoavelmente disponíveis e o contexto do tratamento. Essa distinção está registrada em [[LGPD e Proteção de Dados na IA Generativa]] e permanece sujeita à verificação jurídica.

### Direitos autorais e propriedade intelectual

O guia recomenda verificar se os conteúdos
gerados respeitam direitos autorais
e propriedade intelectual antes de sua
incorporação a materiais oficiais.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 355 e 367–370.

### Segurança e responsabilidade institucional

Nas considerações finais, o guia reforça
a prioridade da segurança da informação,
o respeito à privacidade e à LGPD
e a cautela com plataformas externas
não homologadas.

**Referências:** [[guia-ia-generativa-normalizado]],
linhas 484–490.

## 3. Análise crítica — elaboração editorial

A proteção das informações depende
não apenas da ferramenta escolhida,
mas também do conteúdo efetivamente
incluído nos prompts, nos anexos e nas interações.

É necessário distinguir, para fins
de avaliação operacional:

- Credenciais e identificadores institucionais.
- Dados pessoais e dados pessoais sensíveis.
- Informações internas, restritas ou sigilosas.
- Conteúdos sujeitos a direitos de terceiros.
- Informações aparentemente isoladas
  que, quando combinadas, podem revelar dados protegidos.

A aprovação institucional de uma ferramenta
não significa autorização irrestrita
para inserir qualquer categoria de dado.

**Ressalva sobre ferramentas — REV-004:** a aprovação institucional deve ser interpretada no contexto da finalidade autorizada, das categorias de informação e dos controles efetivamente aplicáveis. Não se pode presumir que toda ferramenta aprovada ofereça as mesmas garantias de confidencialidade, retenção, auditabilidade ou proteção de dados.

O guia também apresenta afirmações sobre transparência e possíveis exceções regulatórias aplicáveis a modelos de código aberto, sem explicitar suficientemente a base normativa ou a jurisdição correspondente. Essas afirmações não devem ser tratadas como regras jurídicas brasileiras automaticamente aplicáveis. Ver [[Normas e Orientações Institucionais para IA Generativa]].

Da mesma forma, substituir nomes por códigos
não assegura, por si só, anonimização efetiva.
O risco de reidentificação depende do contexto
e da possibilidade de cruzamento de informações.

Essas observações são análise editorial.
Não constituem interpretação jurídica vinculante
nem substituem a classificação oficial
das informações ou as políticas do órgão.

## 4. Procedimento preventivo — proposta editorial

O roteiro abaixo é uma proposta editorial
de apoio à decisão operacional, não um
procedimento oficial obrigatório do guia.

### Etapa 1 — Identificar a informação

Antes de preparar o prompt, identificar
quais dados, documentos, credenciais
e referências institucionais serão utilizados.

Verificar se há informações pessoais,
sensíveis, restritas, sigilosas
ou protegidas por direitos de terceiros.

### Etapa 2 — Verificar a autorização

Confirmar se a ferramenta é autorizada
para a finalidade prevista e para
a categoria de informação envolvida.

Na dúvida, consultar a unidade competente
de segurança, privacidade, tecnologia
ou assessoria jurídica.

### Etapa 3 — Minimizar a exposição

Usar apenas as informações estritamente
necessárias à tarefa.

Quando adequado, substituir dados reais
por exemplos fictícios ou simulados.

Não presumir que pseudonimização,
remoção de nomes ou fragmentação
eliminem todos os riscos de identificação.

### Etapa 4 — Avaliar o ambiente

Considerar, conforme as regras aplicáveis:

- Local de processamento e armazenamento.
- Retenção de prompts, arquivos e respostas.
- Possibilidade de compartilhamento com terceiros.
- Uso posterior dos dados para treinamento.
- Controles de acesso e registros de auditoria.

Esses critérios constituem detalhamento
editorial de apoio à avaliação institucional.

### Etapa 5 — Examinar o resultado

Antes de reutilizar ou divulgar a resposta,
verificar se ela expõe dados protegidos,
reconstitui informações confidenciais
ou reproduz material sujeito
a direitos autorais.

A validação do conteúdo é detalhada em
[[Revisão Humana e Validação de Conteúdo]].

### Etapa 6 — Registrar e encaminhar

Quando exigido pelas políticas internas,
registrar a ferramenta utilizada,
a autorização pertinente e as verificações.

Em caso de dúvida ou possível incidente,
encaminhar a situação aos responsáveis
institucionais competentes.

## 5. Critérios de verificação — proposta editorial

Como apoio à revisão operacional, verificar:

- Finalidade do uso identificada.
- Ferramenta aprovada para o contexto.
- Credenciais institucionais protegidas.
- Categoria dos dados examinada.
- Informações inseridas minimizadas.
- Riscos de identificação e agregação avaliados.
- Condições de tratamento dos dados verificadas.
- Direitos de terceiros considerados.
- Resultado revisado antes da divulgação.
- Dúvidas e incidentes encaminhados
  segundo as políticas institucionais.

A aplicação dos critérios depende
das regras internas, do contexto
e da criticidade das informações.

## 6. Conexões com a Wiki

- [[Boas Práticas]] — mapa do eixo.
- [[Governança e Proteção de Dados na IA Generativa]] —
  políticas e controles institucionais.
- [[Conduta Institucional e Responsabilidade]] —
  conduta e deveres do usuário.
- [[Revisão Humana e Validação de Conteúdo]] —
  verificação dos resultados.
- [[Supervisão Humana e Responsabilidade]] —
  controle e decisão humana.
- [[Transparência e Auditabilidade da IA Generativa]] —
  registros e prestação de contas.
- [[Governança]] — princípios de governança.

## 7. Rastreabilidade

- Fonte cadastrada: [[FONTE-001]]
- Documento: [[guia-ia-generativa-normalizado]]
- Proteção inicial: linhas 248–267
- Credenciais: linhas 344–351
- Dados protegidos: linhas 353–365
- Propriedade intelectual: linhas 367–370
- Seleção de ferramentas: linhas 418–434
- Compartilhamento e agregação: linhas 442–452
- Anonimização e risco de reidentificação: linhas 138–140 e 444–452
- Constatação REV-002: [[LGPD e Proteção de Dados na IA Generativa]]
- Aprovação institucional e tratamento de dados: linhas 420–434
- Transparência e exceções regulatórias: linhas 438–440
- Constatação REV-004: [[Normas e Orientações Institucionais para IA Generativa]]
- Verificação jurídica das constatações REV-002 e REV-004: pendente
- Segurança e privacidade: linhas 484–490
- Cadeia documental: [[PROVENIENCIA]]
- Natureza: síntese e proposta editorial
- Revisão humana: pendente
- Verificação jurídica: pendente

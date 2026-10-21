[![header_guiaia](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-ia-generativa/@@govbr.institucional.banner/b2800532-9528-42f4-b021-805b55ba218f/@@images/2f9ee8df-8a0c-44bb-bf51-a6f6077696fd.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/imagens/header_guiaia/view)

[![A ilustração retrata uma mão mecânica que está prestes a tocar uma mão humana.](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-ia-generativa/@@govbr.institucional.banner/fabc9389-8a7c-4858-a86c-e7c2a071890e/@@images/e1e454e6-ff0d-49c1-ba03-b10802b4a498.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/ilustra01.png/view)

Este guia foi elaborado pela Secretaria de Governo Digital (SGD) e pelo Serviço Federal de Processamento de Dados (SERPRO), como parte das ações do Núcleo de Inteligência Artificial (IA) do Governo, com o propósito de apoiar servidores públicos no entendimento e uso responsável de ferramentas de Inteligência Artificial Generativa (IAG).

Neste guia você encontrará uma visão geral da IAG, explicações claras sobre seus desafios e limitações, além de orientações práticas para o uso ético e eficaz dessas ferramentas no setor público brasileiro.

Este guia apresenta orientações sobre uso de Inteligência Artificial Generativa (IAG) no setor público, incluindo descrição dos modelos, riscos, boas práticas e critérios de escolha de ferramentas. O conteúdo será atualizado conforme alterações normativas e evolução tecnológica.

![Infográfico miniatura das boas práticas do Framework AIE](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/infog_bper_mini_amplia_def.png)

Você pode baixar aqui um **PDF com infográficos** que sintetizam as principais **boas práticas e riscos** associados ao uso da **IA generativa** no setor público.  
  
[Download](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/infograficos_defeso.pdf/@@download/file)

## O que é IA Generativa?

[![oqueE.jpg](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-ia-generativa/@@govbr.institucional.banner/e7e02cdc-385b-4e95-bb13-5b35d944f0fb/@@images/1331e8e0-f575-47da-a209-a3f9bc26d1e9.png)](https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/central-de-qualidade/labq/imagens/oquee.jpg/view)

A Inteligência Artificial Generativa é um ramo da inteligência artificial projetado para criar conteúdos, como textos, áudios, imagens, vídeos e até códigos de software. Essa tecnologia se baseia em modelos computacionais avançados, que aprendem padrões a partir de grandes volumes de dados. As ferramentas generativas atualmente mais conhecidas são os LLMs - (

Large Language Model,

 ou Modelos de linguagem de grande escala) que tem como função central que geram textos de maneira natural, semelhante à humana.

Os LLMs, como ChatGPT, Copilot, LLaMA e Gemini, funcionam por meio de uma 
**estrutura de probabilidades**
, na qual procuram replicar com a maior precisão possível a maneira como a linguagem humana é utilizada. O modelo constrói respostas de forma incremental, reconhecendo a entrada fornecida pelo usuário (chamada 
prompt
) e avaliando qual é a sequência de texto mais parecida com a de um ser humano no sentido estatístico. 
No entanto, é fundamental notar que as respostas da IAG não se baseiam em uma compreensão real de contexto, significado ou experiência. Por essa razão, a IAG pode cometer erros factuais convincentes, chamados 
**"alucinações".**

Apesar de todo potencial da IA, inclusive para a realização de tarefas complexas, é sempre importante lembrar que **essa tecnologia não substitui o papel dos humanos na revisão e análise dos resultados obtidos****.** Afinal, nem sempre os resultados produzidos com a ajuda da IA são confiáveis, previsíveis ou explicáveis, especialmente nos modelos de IA mais recentes que são baseados em probabilidades, ou seja, sempre existe a chance da resposta não ser adequada.

Para fazer uma rápida comparação, os programas tradicionais de computador que você já conhece funcionam como se fosse uma calculadora: 2+2 sempre será igual a 4. Já em um sistema que funcione utilizando IA, o resultado de 2+2 pode ser igual ou diferente de 4. Vai depender se o modelo de IA foi treinado com uma base de dados com informações corretas ou incorretas. Por esse motivo todo sistema de IA carrega algum grau de risco, e por isso também a **revisão dos resultados por parte do usuário** é tão importante.

A diferença essencial entre a IAG e a IA Analítica (ou Preditiva) reside em seus objetivos. **A****IA Analítica** utiliza o aprendizado de máquina para **processar grandes quantidades de dados existentes** para **gerar previsões, recomendações ou classificações****.** Seu foco é fazer inferências e prever um estado futuro (como a previsão de crimes ou detecção precoce de doenças) para fornecer suporte à decisão humana (Inteligência Assistida). Em contraste, a **IA Generativa** não se limita a analisar dados, mas sim a **produzir algo novo** (texto, imagem, áudio), dedicando-se à **criação de conteúdo sintético** através dos padrões que internalizou durante o treinamento.

Os grandes modelos generativos de IA são um exemplo típico de Modelo de IA de Finalidade Geral, por permitirem a geração flexível de conteúdo, como texto, áudio, imagens ou vídeo, e podem se adaptar a uma ampla gama de tarefas distintas. Outros exemplos de IAG incluem modelos que produzem imagens a partir de texto (como DALL-E, Midjourney e Stable Diffusion).

No setor público, as ferramentas de IAG oferecem oportunidades para modernizar processos, como automação de tarefas repetitivas, redação de documentos, criação de resumos de documentos e criação de materiais visuais. Contudo, sua adoção deve ser feita de forma criteriosa, garantindo que os benefícios superem os riscos e o uso esteja alinhado com valores éticos e regulatórios.

Modelos de inteligência artificial passam normalmente por ciclos compostos por duas grandes fases: **treinamento** – onde ocorre o ajuste e captura de padrões nos dados, e **produção** - fase da aplicação. Durante a fase de treinamento, esses modelos são expostos a dados diversos, como documentos, imagens e outras fontes públicas ou privadas, para identificar relações e estruturas. Assim, conseguem gerar conteúdos que parecem ter sido criados por humanos. Por exemplo, podem criar um relatório, compor um texto ou gerar um design com base em comandos específicos fornecidos por usuários.

Outra característica importante é que a IAG funciona com base em probabilidade e padrões, e não possui "consciência" ou "intenção". Isso significa que, embora seja uma ferramenta poderosa, ela pode gerar respostas que, em alguns casos, não são adequadas ou estão fora de contexto, o que exige atenção e validação por parte dos usuários.

É crucial entender que, como esses modelos dependem dos dados com os quais foram treinados, eles podem reproduzir vieses ou informações imprecisas presentes nesses dados. Isso reforça a necessidade contínua de supervisão humana e de uma avaliação cuidadosa de suas aplicações, especialmente em instituições públicas que lidam com informações sensíveis e de impacto social.

## Modelos de IA Generativa

Os modelos de IAG podem ser classificados por licenças 
**abertas** 
ou 
**fechadas**
. A diferença entre eles está diretamente relacionada à forma como podem ser utilizados e adaptados às necessidades específicas de cada contexto.

Enquanto os modelos fechados são projetados para oferecer soluções padronizadas e práticas, os modelos abertos se destacam pela flexibilidade, permitindo personalizações e maior controle por parte dos usuários. A escolha entre eles depende das necessidades do projeto, dos recursos disponíveis e das preocupações éticas envolvidas.

Em termos de desempenho, os modelos fechados frequentemente oferecem resultados otimizados em tarefas gerais devido ao alto investimento das empresas de tecnologia em infraestrutura e treinamento contínuo. Já os modelos abertos, embora demandem mais esforço para ajustes, podem superar os fechados em casos de uso específico, especialmente quando adaptados com dados internos.

A escolha entre os dois tipos de modelos deve equilibrar a disponibilidade de recursos, eficiência, privacidade, custo e a necessidade de personalização, garantindo que as ferramentas de IAG sejam usadas de forma responsável e alinhada aos objetivos institucionais.

## Modelos fechados

[![Ilustração vetorial, em estilo plano e com contornos brancos, de um robô humanoide visto de frente. O robô veste uma armadura futurista com um esquema de cores predominante em azul-claro, azul-marinho e verde-limão. O detalhe central de seu torso é uma grande porta de cofre retangular, que possui dobradiças amarelas na lateral esquerda e um grande mostrador circular amarelo com o orifício de uma fechadura preta no centro. A cabeça do robô é arredondada, lembrando um capacete, com um visor único central e detalhes laterais amarelos. Os braços e pernas são revestidos por placas de metal coloridas, e as mãos estão relaxadas ao lado do corpo. Fundo branco.](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-ia-generativa/@@govbr.institucional.banner/ad1cd647-81a7-45e6-975e-4194a60ee405/@@images/74b37ede-1795-431b-b469-10bf6300e498.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/fullmodelo_fechado.png/view)

Desenvolvidos principalmente por grandes empresas como OpenAI, Google e Anthropic, são amplamente utilizados para aplicações como assistentes em bases de conhecimento e bases de dados, auxílio na geração de relatórios padronizados, e automação de atendimento.

Esses modelos geralmente são acessados por meio de APIs, o que facilita sua integração em sistemas existentes e permite que as instituições utilizem suas funcionalidades sem a necessidade de infraestrutura complexa.

No mercado brasileiros, para modelos fechados destaca-se a Maritaca IA, que fornece um modelo treinado, utilizando bases de língua portuguesa, e que pode atender às demandas locais com um custo reduzido e performance equivalente a essas outras soluções. 

Atualmente, os modelos dessas empresas que oferecem os melhores benchmarks e desempenhos são: o GPT-4o, GPT-5 e o3-mini da OpenAI, o Gemini do Google, e o Claude da Anthropic, manus da Manus AI. Apesar das vantagens em desempenho e da facilidade no uso, os modelos fechados apresentam desafios importantes. Muitas vezes, seu uso implica o envio de dados para servidores localizados no exterior, o que pode representar riscos à privacidade e à conformidade com regulamentos locais como a Lei Geral de Proteção de Dados, dentre outras. Além disso, esses modelos funcionam como “caixas pretas”, dificultando auditorias e adaptações, o que pode ser uma limitação para instituições públicas que lidam com informações sensíveis ou que precisam de maior transparência.

## Modelos abertos

[![Ilustração vetorial de corpo inteiro de um robô humanoide futurista, em posição de três quartos voltada para a esquerda. O robô possui um estilo plano (flat design) com contornos brancos e uma paleta de cores em azul-acinzentado, verde e cinza-escuro. A cabeça é envolta por um domo transparente que revela um cérebro estilizado com conexões de rede neural em amarelo; os olhos são representados por dois círculos amarelos. No centro do peito, uma placa exibe um ícone de circuito ou microchip amarelo. Os membros são segmentados e articulados, transmitindo uma aparência tecnológica e cibernética.](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-ia-generativa/@@govbr.institucional.banner/e8c9ab2e-4f40-43a0-ba6a-9e22e13be822/@@images/060cdb99-69b6-4817-804a-63de27d8bdf1.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/fullmodelo_aberto.png/view)

Desenvolvidos principalmente por empresas como a Meta, com o LLaMA 4, pela europeia Mistral AI, com o Mistral 7B, pelo DeepSeek, com o DeepSeek-R1, e pelo Alibaba Cloud com o Qwen-2.5, esses modelos oferecem vantagens significativas para quem busca maior controle e flexibilidade. Esses modelos são disponibilizados sob licenças abertas, permitindo que sejam utilizados e ajustados para atender a contextos específicos e podem ser instalados e executados em servidores locais, eliminando a necessidade de enviar dados para terceiros e garantindo a segurança de informações sensíveis. No Brasil, a Maritaca AI destaca-se com o Sabia-7B, voltado para o idioma português, demonstrando performance equivalente a um custo reduzido.

A Hugging Face se tornou a principal plataforma para acesso a esses modelos abertos. Com suporte dessa plataforma, os usuários podem acessar esses modelos, fazer instalações locais, e realizar customizações tanto locais como diretamente na plataforma, permitindo que os usuários possam utilizar esses modelos de modo simplificado sem necessidade de treinamento do zero.

Esses modelos são disponibilizados sob licenças abertas e podem ser ajustados para atender a contextos específicos, sendo executados em servidores locais para garantir maior segurança e controle sobre os dados. A plataforma Hugging Face oferece também mecanismos para download, fine-tuning e inferência na nuvem de forma simplificada, permitindo que os órgãos possam utilizar esses modelos pré-treinados sem precisar de infraestrutura própria.

## Geração aumentada via recuperação

Como tendência na área da IAG podemos destacar a Geração Aumentada via Recuperação - RAG (Retrieval-Augmented Generation). Trata-se de uma das inovações mais promissoras para lidar com gestão de conhecimento nesse contexto. RAG é uma técnica que combina síntese de texto com recuperação de informação, integrando uma base de conhecimento ao modelo de IAG. Isso permite respostas mais precisas e contextualmente aderentes, ao complementar a capacidade do LLM com dados mais relevantes.

Com o RAG, o modelo não é ajustado diretamente, mas combinado a sistemas de informações que fornecem bases de dados que podem ser consultadas para a geração de respostas. Embora os modelos fechados sejam projetados para tarefas generalistas, eles também podem ser integrados a dados próprios de uma instituição por meio de técnicas como RAG.

## Princípios Fundamentais para o Uso da IAG

**Legalidade:** o uso da IAG deve estar em conformidade com as leis vigentes, incluindo a Lei Geral de Proteção de Dados (LGPD) e demais normativos, garantindo que os direitos dos cidadãos sejam respeitados.

**Impessoalidade:** decisões assistidas por IAG devem ser imparciais, baseadas em critérios objetivos e livres de viés ou preconceito.

**Moralidade (Ética):** essencial no uso de IAG, assegurando transparência, justiça e respeito aos direitos humanos e às garantias democráticas.

**Publicidade:** os processos envolvendo IAG devem ser transparentes, permitindo auditoria e contestação quando necessário.

**Eficiência:** ferramentas de IAG devem ser usadas para automatizar tarefas repetitivas, liberando recursos para atividades mais estratégicas, desde que sempre com revisão humana.

## Riscos

[![Banner Riscos](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/riscos_b_1.png/@@images/92e2efc3-2102-41e4-ace7-8fa0c478e280.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/riscos_b_1.png/view)


Riscos Inerentes à IA Generativa

[![Banner Riscos 2](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/riscos_b_2.png/@@images/0e074cc7-a16f-410b-bf01-5839752df9f2.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/riscos_b_2.png/view)


Riscos Inerentes à IA Generativa

Antes de utilizar ferramentas de IAG em processos de trabalho, é necessário analisar os benefícios e riscos associados a cada caso de uso. A identificação das vulnerabilidades específicas e a implementação de medidas de mitigação são passos indispensáveis para garantir que as ferramentas sejam usadas de forma ética e segura. O uso de IAG está sujeito a riscos inerentes, como:

Alucinações na IA Generativa

Modelos de IAG são treinados em grandes volumes de dados e podem produzir respostas “criativas” baseadas em padrões e informações aprendidas durante um longo processo de treinamento. Entretanto, essa criatividade sintética pode desencadear alucinações – situações em que um modelo de inteligência artificial gera informações inexatas, irrelevantes ou totalmente fabricadas, mesmo que pareçam confiáveis e coerentes. Esse comportamento surge devido a limitações nos dados de treinamento, dados de entrada e na arquitetura do modelo, tais como:

**Perguntas mal formuladas:** questões ambíguas ou abertas podem levar a respostas imprecisas.

**Dados incompletos ou enviesados:** o modelo pode basear sua resposta em informações limitadas ou distorcidas presentes no conjunto de dados.

**Tendência a completar informações:** quando não encontra uma resposta clara, o modelo pode "criar" com base em dados relacionados. Modelos de IAG também podem gerar textos e apontar referências inexistentes, o que não é aceitável para a segurança da informação veiculada.

**Falta de atualização:**  os modelos são treinados com dados disponíveis até uma determinada data e, após isso, não conseguem incluir automaticamente informações mais recentes. Isso significa que, para assuntos contemporâneos ou em constante evolução, as respostas podem estar desatualizadas.

Implicações Legais

É essencial que o uso de ferramentas de IAG seja acompanhado de uma avaliação rigorosa sobre a origem e a natureza dos dados gerados, garantindo que estejam em conformidade com a legislação e as boas práticas institucionais. Este item aborda os cuidados necessários em relação ao uso de ferramentas de IAG, considerando aspectos legais e éticos ligados a direitos autorais e propriedade intelectual.

**Dados Protegidos:** muitas ferramentas de IAG são treinadas com dados que podem estar protegidos por direitos autorais e propriedade intelectual. Embora a coleta e o tratamento desses dados possam ser legais, nem sempre isso é garantido. Os sistemas de IA podem violar a LGPD, a Lei de Direitos Autorais ou outras leis de privacidade.

**Obras Protegidas:** trechos de textos, imagens ou outros conteúdos gerados pela IAG podem conter elementos derivados de obras protegidas, expondo o órgão a riscos jurídicos e reputacionais.

**Responsabilidade:** Ainda que a IAG possa ser usada na automação de uma atividade no trabalho, a responsabilidade final sobre a produção do conteúdo é do servidor, cabendo a ele a revisão e validação do material produzido dentro dos princípios da administração pública.

Vazamento de Dados, Ataques e Acessos Não Autorizados

O uso de modelos de inteligência artificial generativa pode expor organizações e usuários a uma série de riscos relacionados à segurança da informação, caso não sejam adotadas práticas robustas de mitigação.

**Vazamento de Dados:** modelos generativos treinados em grandes volumes de dados podem, inadvertidamente, restituir informações sensíveis presentes no conjunto de dados original, especialmente se os dados não foram devidamente anonimizados. Além disso, práticas inadequadas de armazenamento e compartilhamento podem expor informações pessoais ou confidenciais.

**Ataques cibernéticos com IA:** a IA generativa pode ser usada para criar phishings, áudios ou vídeos falsos (deepfakes) que tornam golpes mais convincentes. É essencial reforçar a cibersegurança e capacitar servidores para reconhecer e prevenir essas ameaças.

**Envenenamento de dados:** ocorre quando informações falsas ou manipuladas são inseridas nos conjuntos usados para treinar modelos de IA, comprometendo seus resultados e decisões. Esse risco exige **controle rigoroso da origem e qualidade dos dados**, além de **monitoramento contínuo** para garantir integridade e confiabilidade nos sistemas utilizados pelo setor público.

Importância da Anonimização de Dados

A anonimização de dados é uma prática essencial para garantir que as informações pessoais e sensíveis não sejam vinculadas a indivíduos ou entidades específicas, reduzindo o risco de exposição acidental. Técnicas como mascaramento, tokenização, generalização e substituição de dados reais por sintéticos são recomendadas para proteger a privacidade dos indivíduos.

Viés na IAG

Apresentado como uma questão central devido à dependência dos modelos de IAG de grandes volumes de dados de treinamento. Esses dados podem conter preconceitos implícitos, desigualdades ou representações inadequadas, que acabam sendo refletidos nos resultados gerados.

**Viés de Contexto:** ocorre quando a IA falha em interpretar ou aplicar os dados corretamente em contextos diferentes daquele em que foi treinada. Pode ser considerado um viés de contexto linguístico e cultural quando as diferenças de idioma, gírias, dialetos ou contextos culturais não são capturados. Ex.: interpretar incorretamente expressões regionais ou termos indígenas brasileiros.

**Viés de Automação:** é a tendência de confiar nas decisões automatizadas da IA como sendo sempre precisas ou imparciais, mesmo quando estão incorretas.

**Viés de Representatividade:** dados de treinamento que não representam adequadamente a diversidade podem fazer com que o modelo funcione bem para alguns grupos, mas mal para outros.

**Viés de Seleção:** ocorre quando os dados usados no treinamento não são suficientemente aleatórios ou representativos, resultando em uma amostra enviesada.

**Viés de Exclusão:** grupos sub-representados ou excluídos do conjunto de dados acabam sendo ignorados, ou mal interpretados pela IA. O modelo tende a reforçar padrões já dominantes nos dados, sem considerar alternativas. Ex.: associar automaticamente enfermeiras a mulheres, porque essa associação é mais frequente nos textos de treinamento.

**Viés Histórico:** quando os dados refletem desigualdades e preconceitos já existentes na sociedade.Ex.: modelos de recrutamento que repetem discriminações de gênero ou raça presentes em dados antigos.

**Viés Algorítmico:** Introduzido pelo próprio design do algoritmo (ponderação de variáveis, funções de custo, priorização de certas saídas). Ex.: um sistema de recomendação que privilegia conteúdos mais populares, invisibilizando produções de nicho.

**Viés de Interação (ou Feedback):** Ocorre quando o uso contínuo pelos usuários reforça vieses já existentes. Ex.: se usuários aprovam respostas estereotipadas, o modelo “aprende” a replicá-las mais.

## Classificação de Riscos

O Projeto de Lei nº 2338/2023 em discussão no Congresso Nacional busca estabelecer um marco regulatório para o desenvolvimento e uso de sistemas de inteligência artificial (IA) no Brasil. A proposta estabelece uma classificação dos riscos da IA adequando as exigências conforme o potencial impacto dos sistemas. Com base nesse projeto, esta cartilha adota uma categorização que define riscos excessivos, altos riscos e demais riscos, determinando o regime jurídico aplicável e as obrigações correspondentes para garantir a segurança, transparência e proteção dos direitos fundamentais.

Risco Excessivo

> o **PL 2338/2023** propõe a proibição do desenvolvimento e uso de sistemas de inteligência artificial que apresentem riscos excessivos à sociedade e aos direitos fundamentais. São considerados de risco excessivo e vedados os sistemas de IA que:

Induzam ou manipulem comportamentos de forma prejudicial à saúde, segurança ou direitos fundamentais.

Explorem vulnerabilidades de grupos vulneráveis (ex.: crianças, idosos, pessoas com deficiência) para influenciar ou causar danos.

Realizem perfis preditivos criminais, avaliando características pessoais para prever crimes ou reincidência.

Sejam utilizados pelo poder público para pontuação social, classificando cidadãos com base em seu comportamento ou personalidade de maneira discriminatória.

Façam identificação biométrica em tempo real em espaços públicos, salvo exceções (ex.: busca de pessoas desaparecidas).

Alto Risco

> Apesar desses sistemas **não serem proibidos**, o seu uso deve ser cuidadosamente monitorado e controlado para evitar abusos, discriminações ou danos irreversíveis, podendo gerar impactos significativos sobre direitos fundamentais, segurança, privacidade e bem-estar da sociedade. Dessa forma, a categorização de alto risco impõe obrigações regulatórias mais rígidas e medidas específicas de governança, exigindo avaliação de impacto algorítmico, transparência, supervisão humana e mitigação de riscos, garantindo que a IA seja usada de forma ética e responsável. São considerados de alto risco os sistemas de IA utilizados em:

Uso em segurança para gestão de infraestruturas críticas, como trânsito e redes de abastecimento.

Aplicações na educação e formação profissional, incluindo acesso e avaliação de estudantes.

Uso em recrutamento, triagem, avaliação de candidatos, gestão e monitoramento no trabalho.

Avaliação de elegibilidade e concessão de serviços públicos e privados essenciais.

Análise da capacidade de endividamento e classificação de crédito.

Definição de prioridades para serviços de emergência, como bombeiros e assistência médica.

Apoio à administração da justiça, investigação e aplicação da lei.

Uso de veículos autônomos com riscos à integridade física.

Aplicações na saúde, incluindo diagnósticos e procedimentos médicos.

Uso de sistemas biométricos de identificação.

Investigação criminal e segurança pública, incluindo avaliação de riscos e perfis criminais.

Análise de crimes por meio de grandes conjuntos de dados para identificar padrões.

Investigação administrativa para avaliar provas e prever infrações com base em perfis.

Gestão da migração e controle de fronteiras.

Risco Moderado

> Abrange sistemas que **apresentam impacto significativo**, mas **não tão elevado quanto os sistemas classificados como de alto risco**. Esses sistemas podem afetar a vida das pessoas de maneira relevante, porém o potencial de dano é limitado ou controlável, não sendo considerado grave o suficiente para justificar um nível de regulamentação tão rigoroso quanto os de risco alto ou excessivo. Entretanto, exige-se a implementação de medidas de transparência, explicabilidade e supervisão, mas com menos rigidez do que os sistemas de alto risco. Exemplos de sistemas de risco moderado incluem:

IA em áreas como recursos humanos, por exemplo, para triagem inicial de currículos ou entrevistas automatizadas, onde as decisões são importantes, mas não definitivas.

Sistemas de recomendação em comércio eletrônico, que influenciam o consumo, mas sem implicações diretas na saúde, liberdade ou outros direitos fundamentais dos indivíduos.

Análise de dados em setores como marketing ou publicidade, nas quais a IA é usada para personalizar ofertas, mas sem invadir a privacidade de forma invasiva.

Geração ou manipulação de texto, imagem, áudio ou vídeo — especialmente se pode causar confusão ou engano (por exemplo, deepfakes de figuras públicas).

Baixo Risco

> Esses sistemas não exigem medidas rigorosas de regulação, **mas ainda devem cumprir requisitos básicos de transparência, responsabilidade e boas práticas de governança**. Embora esses sistemas tenham baixo potencial de dano, a lei ainda exige que sejam transparentes quanto ao seu funcionamento, especialmente quando interagem diretamente com pessoas, para garantir que os usuários saibam quando estão lidando com IA e possam tomar decisões informadas. Alguns exemplos incluem:

Chatbots e assistentes virtuais, que interagem com usuários sem tomar decisões com consequências jurídicas ou econômicas relevantes.

Filtros de recomendação, como os usados em plataformas de streaming e comércio eletrônico, para sugerir conteúdos ou produtos com base em preferências do usuário.

Ferramentas de edição de imagem e vídeo, que modificam conteúdos visuais sem comprometer direitos fundamentais.

Jogos e aplicações recreativas, que utilizam IA para melhorar a experiência do usuário sem riscos significativos.

## Recomendações e boas práticas

[![Boas Práticas 1](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/boas_c_1.png/@@images/41ac29e6-57ae-474e-ace5-e96b6da28950.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/boas_c_1.png/view)


Cuidados com conteúdo e proteção de dados e informações

[![Boas Práticas 2](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/boas_c_2.png/@@images/77f88254-6ba3-43db-a6e2-439e157426d7.png)](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/boas_c_2.png/view)


Os "Três Comos" e boas práticas de tecnologia e segurança

Ao lidar com IAG, é necessário adotar uma abordagem consciente para evitar riscos como o vazamento de dados sensíveis, disseminação de informações enganosas e interpretações equivocadas de resultados. Isso reflete um compromisso com a ética, a privacidade e a segurança, especialmente no contexto da administração pública. Para promover uma cultura de responsabilidade no uso dessas ferramentas, algumas regras básicas devem ser seguidas:

**Evitar informações sensíveis:** ao compartilhar informações sensíveis ou dados pessoais, lembre-se que a segurança desses dados depende de vários fatores. Consulte as políticas de privacidade dados sensíveis e pessoais e cuidado ao compartilhar tais informações.

**Os três "Como" a considerar:** 
> **Como as perguntas serão usadas:** evite inserir informações que você não compartilharia publicamente, considerando que a ferramenta aprende com os dados fornecidos.
>
> **Como as respostas podem ser enganosas:**As respostas da IA, embora pareçam confiáveis, podem ser imprecisas ou derivadas de fontes não verificadas, exigindo validação rigorosa.
>
> **Como a IA funciona:** ss respostas são geradas probabilisticamente, sem compreensão de contexto ou viés, necessitando interpretação criteriosa.

**Consultas especializadas:** servidores públicos devem buscar orientação de serviços jurídicos e especialistas em privacidade e segurança de dados e informações para decidir sobre o uso adequado dessas ferramentas.

**Priorize Soluções Aprovadas:** o servidor deve priorizar o uso de ferramentas de IAG disponibilizadas internamente pela instituição pois estas geralmente possuem recursos de segurança que mitigam riscos de vazamento de dados e informações sensíveis protegidas legalmente.

**Revisão Humana Inegociável:**  a IAG **deve ser uma ferramenta auxiliar**, não substituta, mantendo-se sempre o **controle humano** sobre o processo criativo e decisório. O usuário é o **responsável integral** por qualquer documento ou decisão produzida, com ou sem o uso da IAG. É crucial haver **revisão crítica e criteriosa** de todo conteúdo gerado pela IA, mesmo que ele pareça confiável, para garantir precisão e adequação.

**Evite Decisões Estratégicas:** não é recomendado o uso de IAG para **tomada de decisões estratégicas** ou para funções complexas como **predição/previsão** de cenários e dados que exijam análise humana profunda, devido aos riscos de erros, incertezas ou viés de automação.

**Cuidados com o compartilhamento de informações oficiais:** além do cuidado sobre a tomada de decisão estratégia, evite inserir dados sobre decisões oficiais de caráter sigiloso.

**Conteúdo para o Público Externo:** deve-se evitar o uso de IAG externa para a produção de conteúdo voltado ao público externo ou para o fornecimento de informações diretamente a ele, sem um processo rigoroso de revisão humana.

A partir dessas regras iniciais, as seguintes orientações devem ser consideradas em relação a boas práticas:

Revisão Institucional

> **O uso de IAG deve passar por revisão institucional, considerando os princípios éticos, os riscos e as melhores práticas definidos internamente pelo órgão.**

Revisar o conteúdo gerado para garantir alinhamento com princípios institucionais. Analise a resposta dos prompts de IAG para garantir que eles atendam os padrões da Instituição quanto aos princípios éticos, de legalidade, e adequação.
> **Bom uso:** Rever a resposta de IAG e ajustar para alinhamento com os valores institucionais antes da publicação.
>
> **Uso não aconselhável:** Publicar diretamente conteúdos gerados, sem revisão, especialmente em temas sensíveis.

Sempre avalie criteriosamente e revise o conteúdo gerado por IAG, ainda que a resposta pareça confiável.
> **Bom uso:** Testar a IAG para gerar rascunhos e verificar cada ponto factual antes de aceitar o conteúdo respondido.
>
> **Uso não aconselhável:** Aceitar respostas de IAG como verdadeiras sem verificá-las, principalmente em relação a tópicos técnicos ou científicos envolvendo operações matemáticas.

Decisões Automatizadas

> **Decisões automatizadas pela IAG não devem ser adotadas sem revisão humana, principalmente quando usada para informar o público externo ou quando envolver decisões estratégicas.**

Evite o uso sem validação e considere a capacidade de identificar imprecisões antes de usar a IAG.
> **Bom uso:** Solicitar apoio de especialistas na validação de conteúdos gerados por IA antes de sua publicação.
>
> **Uso não aconselhável:** Utilizar conteúdos técnicos complexos gerados por IA sem consultar especialistas na área.

Sempre avalie criteriosamente e revise o conteúdo gerado por IAG, ainda que a resposta pareça confiável.
> **Bom uso:** Testar a IA para gerar rascunhos e verificar cada ponto factual antes de aceitar o conteúdo respondido.
>
> **Uso não aconselhável:** Aceitar respostas de IA como verdadeiras sem verificá-las, principalmente em relação a tópicos técnicos ou científicos envolvendo operações matemáticas.

Conduta Institucional

> **O uso de IAG deve estar alinhado com o código de conduta institucional e as políticas de não discriminação, garantindo que o conteúdo seja apropriado e não discriminatório.**

Avaliar o conteúdo da resposta da IA para garantir que não discrimine indivíduos com base em raça, cor, religião, sexo, nacionalidade, idade, deficiência, estado civil, afiliação política ou orientação sexual.
> **Bom uso:** Usar IA para criar descrições inclusivas, validando que a linguagem não perpetue estereótipos.
>
> **Uso não aconselhável:** Utilizar conteúdo sem avaliação, resultando em mensagens discriminatórias
> ou tendenciosas.

Conteúdo Inapropriado

> **Para proteger servidores, cidadãos e a instituição, recomenda-se evitar o uso de conteúdo criado pela IA que seja inapropriado, discriminatório, incorreto ou prejudicial.**

Revisar o conteúdo gerado para garantir alinhamento com princípios institucionais. Analise a resposta dos prompts de IAG para garantir que eles atendam os padrões da Instituição quanto aos princípios éticos, de legalidade, e adequação.
> **Bom uso:** Rever a resposta de IAG e ajustar para alinhamento com os valores institucionais antes da publicação.
>
> **Uso não aconselhável:** Publicar diretamente conteúdos gerados, sem revisão, especialmente em temas sensíveis.

Avaliar o conteúdo da resposta da IA para garantir que não discrimine indivíduos com base em raça, cor, religião, sexo, nacionalidade, idade, deficiência, estado civil, afiliação política ou orientação sexual.
> **Bom uso:** Usar IA para criar descrições inclusivas, validando que a linguagem não perpetue estereótipos.
>
> **Uso não aconselhável:** Utilizar conteúdo sem avaliação, resultando em mensagens discriminatórias ou tendenciosas.

Sempre avalie criteriosamente e revise o conteúdo gerado por IAG, ainda que a resposta pareça confiável.
> **Bom uso:** Testar a IA para gerar rascunhos e verificar cada ponto factual antes de aceitar o conteúdo respondido.
>
> **Uso não aconselhável:** Aceitar respostas de IA como verdadeiras sem verificá-las, principalmente em relação a tópicos técnicos ou científicos envolvendo operações matemáticas.

Responsabilidade do Servidor

> **A responsabilidade do servidor sobre qualquer documento produzido, com ou sem IAG, permanece inalterada. O uso inadequado de IAG não exime o servidor de revisar e assumir a autoria plena do resultado..**

Identificar a resposta gerada pela IA, sem prejuízo da responsabilização do servidor.
> **Bom uso:** Incluir no rodapé de um documento institucional a observação: “Parte do conteúdo foi gerado com o auxílio de IA.”
>
> **Uso não aconselhável:** Apresentar conteúdo gerado por IA como criação exclusiva de autores humanos, sem a devida transparência.

Sempre avalie criteriosamente e revise o conteúdo gerado por IAG, ainda que a resposta pareça confiável.
> **Bom uso:** Testar a IAG para gerar rascunhos e verificar cada ponto factual antes de aceitar o conteúdo respondido.
>
> **Uso não aconselhável:** Aceitar respostas de IAG como verdadeiras sem verificá-las, principalmente em relação a tópicos técnicos ou científicos envolvendo operações matemáticas.

Uso de Credenciais

> **Recomenda-se evitar o uso de endereços de e-mail, credenciais e números de telefone do órgão ou entidade para criar contas em plataformas externas de IAG, prevenindo a ligação entre uso pessoal e trabalho institucional.**

Não use credenciais da instituição, endereços de e-mail ou números de telefone como login para aplicativos de IAG disponíveis publicamente.
> **Bom uso:** Criar contas usando credenciais genéricas, desvinculadas da instituição, para experimentação em IAG.
>
> **Uso não aconselhável:** Usar o e-mail institucional para acessar um serviço de IA, como o ChatGPT ou qualquer prompt semelhante, sem a devida aprovação.

Dados Protegidos

> **Para proteger informações sensíveis e confidenciais, incluindo dados protegidos por lei e propriedade intelectual, é indicado que servidores e prestadores de serviços utilizem apenas soluções de IAG aprovadas pelo órgão.**

Não insira informações internas da instituição em aplicativos de IAG que não seja uma solução aprovada.
> **Bom uso:** Solicitar sugestões de estratégias de gerenciamento genéricas, sem mencionar nomes de projetos ou informações específicas da instituição.
>
> **Uso não aconselhável:** Compartilhar detalhes de contratos, projetos em andamento ou políticas internas ao solicitar sugestões.

Não insira informações pessoais de servidores, cidadãos ou terceiros em aplicativos de IAG não aprovados.
> **Bom uso:** Usar informações fictícias ou simuladas para criar exemplos ou cenários durante testes com IA.
>
> **Uso não aconselhável:**ornecer dados reais de servidores, como CPF ou informações de saúde, para obtenção de insights.

Garanta que os conteúdos gerados respeitem direitos autorais e de propriedade intelectual.
> **Bom uso:** Solicitar à IA conteúdo genérico e verificar sua originalidade antes de incorporá-lo a materiais oficiais.
>
> **Uso não aconselhável:**Usar trechos gerados por IA sem verificar se são plágios ou violações de direitos autorais.

Diante das regras e boas práticas apresentadas, alguns exemplos de utilização das ferramentas de IAG são:

**Elaboração e Revisão de Documentos:** Ajuda na redação de relatórios, comunicados e documentos oficiais, além de revisão gramatical, estilística e tradução de textos.

**Resumo de Textos:** Transformar grandes volumes de texto em resumos claros e diretos.

**Consulta a Normas:** Facilitar o acesso e a interpretação de leis e regulamentos.

**Geração de Conteúdo Multimídia (com cautela):** Pode criar imagens, áudios ou vídeos, mas o servidor deve agir com cautela e responsabilidade, especialmente no que diz respeito a deepfakes (simulação de pessoas reais).

## Alguns exemplos de uso de IA no setor público brasileiro

Seguem alguns exemplos de aplicação:

Controladoria-Geral da União (CGU)

Criou a ferramenta **Alice**, baseada em mineração de texto e inteligência artificial.

Analisa licitações públicas para identificar **possíveis inconsistências**.

Emite **alertas de risco**, por exemplo, quando detecta indícios de **pesquisa de preços com valores excessivos.**

Objetivo: **apoiar o trabalho dos auditores** na detecção de irregularidades.

## Para saber mais

Diversas iniciativas ao redor do mundo têm documentado e disponibilizado casos de uso de Inteligência Artificial no setor público. A seguir, alguns repositórios e observatórios que reúnem experiências práticas e bases de conhecimento sobre o tema:

**União Europeia** – [Public Sector Tech Watch (PSTW)](https://interoperable-europe.ec.europa.eu/collection/public-sector-tech-watch)

Observatório que monitora, analisa e divulga o uso de tecnologias emergentes, como IA e blockchain, no setor público europeu.

**América Latina e Caribe** – [Sistemas de Algoritmos Públicos](https://sistemaspublicos.tech/sistemas-de-ia-en-america-latina/)

Projeto acadêmico da Universidade dos Andes (Colômbia) que mapeia e analisa iniciativas de uso de sistemas algorítmicos por governos da região.

**Estados Unidos** – [Inventário de Casos de Uso de IA](https://www.cio.gov/policies-and-priorities/Executive-Order-13960-AI-Use-Case-Inventories-Reference/)

Repositório mantido pelo Office of Management and Budget e o Chief Information Officer dos EUA, com mais de 1.700 usos de IA em agências federais.

**Reino Unido** – [AI.gov.uk – Knowledge Hub](https://ai.gov.uk/knowledge-hub/use-cases)

Portal do governo britânico que apresenta casos de uso de IA, incluindo ferramentas e soluções de código aberto aplicadas à administração pública.

Essas plataformas são ótimos pontos de partida para quem deseja se inspirar, comparar abordagens ou buscar referências para novas iniciativas com uso de inteligência artificial no setor público.

## Critérios de Escolha de Ferramentas

A escolha da ferramenta deve ser guiada pela **confidencialidade dos dados** a serem tratados e pelo nível de controle e auditabilidade que o órgão público precisa exercer sobre o sistema.

Ferramentas Internas/Locais (Aprovadas)

**Recomendação:** Priorize as soluções internas (locais) ou aquelas fornecidas por terceiros, mas foram **aprovadas pela unidade executiva de TI** do órgão, como o ChatTCU ou CopilotTCU (no contexto do Tribunal de Contas da União), pois estas geralmente possuem recursos de segurança que mitigam riscos de vazamento de dados e informações sensíveis protegidas legalmente.

**Vantagem Principal:** Tais soluções são projetadas para **manter a confidencialidade das informações sigilosas** da instituição e cumprem os requisitos de segurança definidos em normativos internos.

Ferramentas Externas/Comerciais (Fechadas ou em Nuvem)

**Risco Elevado:** As plataformas externas de IAG (como ChatGPT, Gemini, Copilot, etc.) são fornecidas por terceiros e geralmente são consideradas "caixas-pretas" com relação à transparência de seus modelos e uso de dados.

**Governança de Dados:** Deve-se consultar a política de segurança do órgão. Se a ferramenta externa salva, usa posteriormente ou compartilha os dados recebidos para treinar seu modelo, ela não deve ser usada para tratar dados protegidos.

**Privacidade:** Muitos modelos aproveitam as interações dos usuários para treinamento de seus sistemas, o que implica que os dados disponibilizados podem se tornar parte de conjuntos de dados futuros.

Software Livre e Código Aberto (Open Source)

**Transparência:** Modelos de código aberto (open source) promovem maior transparência, pois seus parâmetros e arquitetura são disponibilizados publicamente.

**Exceção à Transparência:** Prestadores de modelos de IAG lançados sob licença gratuita e de código aberto podem ser isentos de certos requisitos de transparência, a menos que o modelo apresente riscos sistêmicos. Mesmo assim, a obrigação de elaborar um resumo dos conteúdos usados no treino e cumprir a legislação de direitos autorais permanece.

Cuidados com o Compartilhamento de Informações Oficiais

A cautela é fundamental, pois o vazamento ou compartilhamento irregular de dados sensíveis, restritos ou sigilosos pode gerar **danos críticos aos cidadãos e à reputação da instituição.**

**Não Insira Dados Pessoais ou Pessoais Sensíveis:** Nunca forneça dados pessoais ou pessoais sensíveis de terceiros (saúde, etnia, religião, opinião política) a ferramentas de IAG. Se o uso for inevitável, utilize informações anonimizadas.

**Proteção de Dados do Órgão:** Não insira **informações internas, restritas ou sigilosas** do órgão em aplicativos externos de IAG.

**Credenciais Institucionais:** Evite usar e-mails, números de telefone ou credenciais institucionais para criar contas em plataformas externas de IAG. Essa prática ajuda a proteger a segurança dos dados da instituição.

**Evitar Agregação de Dados:** Evite inserir informações que permitam às ferramentas públicas **extrapolar informações confidenciais ou classificadas** com base na agregação do conteúdo inserido ao longo do tempo.

Instruções para Prompts

Orientações sobre criaçãoo de instruções (prompts) para uso de ferramentas de IA generativa estão disponíveis no Guia Pratico de Prompt e Pesquisa com IA para Servidores Publicos, publicado pela SGD/MGI: [Guia prático de prompt e pesquisa com IA para servidores públicos — Governo Digital.](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-pratico-de-prompt-e-pesquisa-com-ia-para-servidores-publicos/)

Governança de Dados

As informações do Governo Federal sobre o conjunto de políticas, normas, padrões e práticas que orientam, monitoram e avaliam a gestão e o uso dos dados, para assegurar que sejam utilizados de maneira ética, segura e eficiente, atendendo às necessidades institucionais e regulatórias estão disponíveis na página de [Governança de Dados — Governo Digital.](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/governancadedados)

## Competências Digitais e Capacitação de Servidores

O uso crescente da IAG na Administração Pública exige que os servidores desenvolvam a **Alfabetização em IA (AI Literacy)** e mantenham o **pensamento crítico**. Esta alfabetização inclui competências, conhecimento e compreensão que permitem aos usuários tomar decisões informadas, estando cientes das oportunidades, dos riscos e das limitações da IA.

O letramento em IA é essencial para que os servidores mantenham seu protagonismo no processo científico, utilizando a IA como ferramenta de apoio, mas **sem comprometer sua capacidade crítica e criativa**. O desenvolvimento dessas habilidades deve capacitar o servidor a:

Revisão Crítica

O usuário deve **sempre avaliar e revisar criteriosamente** todo o conteúdo gerado pela IAG, mesmo que pareça confiável, pois a IA não se baseia em uma compreensão real de contexto ou significado. O servidor é o responsável integral por qualquer documento ou decisão final. A colaboração homem-máquina busca aliar a eficiência e a velocidade da IA com o julgamento crítico, o discernimento ético e a responsabilidade legal do ser humano. O ser humano é o elemento de validação final que garante que a tecnologia seja usada de forma justa e alinhada aos valores da administração pública.

Identificação de Falhas (Alucinações e Vieses)

O servidor deve ser capaz de identificar as **"alucinações"** (respostas factualmente incorretas, mas convincentes) e os **vieses** (tendências nos dados de treinamento que influenciam resultados). Os vieses podem levar a **discriminações** contra grupos sub-representados.

Literacia em IA

É fundamental **educar as equipes sobre as capacidades e limitações** da IAG. A excelência dos resultados da IA depende da qualidade dos dados utilizados no treinamento.

Sob esta perspectiva, é possível encontrar cursos de capacitação dos servidores públicos em IA de acordo com os perfis dos cargos que ocupam no link: [Inteligência Artificial — Governo Digital](https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1) , com programas de diversos níveis de conhecimento.

## Considerações finais

Este texto preliminar estabelece os fundamentos e princípios gerais para as boas práticas do uso da Inteligência Artificial generativa no âmbito da administração pública federal. Os pontos visam proteger contra vazamentos de dados, garantir a confidencialidade das informações sigilosas, evitar violações de propriedade intelectual, assegurar a segurança de servidores e cidadãos, prevenir danos à reputação da instituição, mitigar viés de modelos automatizados e evitar infrações de direitos autorais. O cumprimento das orientações desta cartilha contribui para o uso seguro e responsável de sistemas de IA no âmbito da administração publica federal, em conformidade com a legislação vigente.

Toda solução baseada em IA deve considerar a segurança da informação como prioridade, especialmente quando envolve dados sensíveis ou atividades críticas do Estado. A privacidade dos dados pessoais também deve ser respeitada rigorosamente, conforme os princípios da Lei Geral de Proteção de Dados (LGPD) e as boas práticas estabelecidas por órgãos como a ANPD e a CGU. O compartilhamento inadequado de informações pessoais ou sensíveis com sistemas de IA pode não apenas comprometer a segurança institucional, mas também resultar em responsabilização legal e disciplinar dos agentes envolvidos.

Outro aspecto essencial é a supervisão humana. Mesmo em sistemas altamente automatizados, a responsabilidade final sobre decisões, ações e interpretações continua sendo do servidor público. A IA deve ser entendida como uma ferramenta de apoio. Ela pode ampliar a capacidade humana de agir com mais agilidade e inteligência, mas nunca substitui o julgamento ou a responsabilidade de quem a utiliza.

Além dos sistemas institucionais, muitos servidores têm buscado experimentar individualmente ferramentas de IA para melhorar sua produtividade, como na redação de textos, tradução, organização de tarefas ou resumo de conteúdos. Esse uso pode ser positivo, desde que feito com cautela. É fundamental que o servidor não compartilhe dados sensíveis, informações sigilosas ou documentos institucionais com essas plataformas, especialmente quando operam em ambientes externos e não homologados pelo órgão. E, independentemente da ferramenta usada, os conteúdos gerados devem sempre ser analisados criticamente, já que a responsabilidade pelas ações administrativas permanece com o servidor.

Também é importante lembrar que o uso de IA deve ser feito com propósito claro e justificado. Adotar essa tecnologia apenas por modismo ou sem uma necessidade concreta pode resultar em desperdício de recursos, aumento desnecessário da complexidade e baixa efetividade. Toda iniciativa com IA deve considerar o equilíbrio entre custos e benefícios, avaliando se os ganhos realmente justificam o investimento, o esforço de implantação e os riscos envolvidos. Esses riscos não se limitam a falhas técnicas ou imprecisões. Podem envolver vieses nos dados, decisões injustas, falta de transparência nos resultados e impacto negativo sobre pessoas ou grupos vulneráveis. Quanto maior o nível de automação, maior deve ser o cuidado na definição de regras, na curadoria de dados e na validação contínua do sistema.

Outro fator relevante é o impacto ambiental associado ao uso de sistemas de IA, especialmente os mais avançados. O treinamento e operação de modelos complexos consomem grandes volumes de água, energia e demandam recursos computacionais significativos. Por isso, também é essencial avaliar a sustentabilidade das soluções desde a fase de planejamento, optando por abordagens mais eficientes sempre que possível.

Por fim, o desenvolvimento e uso de soluções de IA devem estar alinhados a princípios éticos amplamente reconhecidos. A Recomendação da UNESCO sobre a Ética da Inteligência Artificial estabelece diretrizes para que a adoção dessas tecnologias respeite valores universais e direitos fundamentais. O documento enfatiza a importância da transparência, da proteção à privacidade, da justiça algorítmica, da não discriminação, da inclusão e da explicabilidade das decisões automatizadas. Também reforça que o uso de IA deve ser centrado nas pessoas, contribuindo para o bem-estar coletivo, a equidade e o desenvolvimento sustentável.

Esses princípios devem servir de base para orientar políticas públicas, regulamentações, desenvolvimento de soluções e capacitação de servidores. Incorporar esses valores desde a concepção dos projetos é essencial para que a IA seja aplicada de forma segura, confiável e compatível com os objetivos do Estado democrático.

Este guia foi elaborado no âmbito do Plano Brasileiro de Inteligência Artificial (PBIA), com contribuição técnica da SGD/MGI, SERPRO, Casa Civil, MCTI, ENAP e Dataprev."

## Referências

1. AMÉRICA LATINA E CARIBE. Sistemas de Algoritmos Públicos – Universidade dos Andes. Disponível em:    
   [https://sistemaspublicos.tech/sistemas-de-ia-en-america-latina/.](https://sistemaspublicos.tech/sistemas-de-ia-en-america-latina/) Acesso em: 07 out. 2025.

2. AUSTRALIAN GOVERNMENT ARCHITECTURE. Interim guidance on government use of public generative AI tools. November 2023. Disponível em: <https://architecture.digital.gov.au/guidance-generative-ai>. Acesso em: 31 jan. 2025.

3. BRASIL. Receita Federal. Instrução Normativa RFB nº 2.134, de 10 de março de 2023. Disponível em: <http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=138693>. Acesso em: 31 jan. 2025.

4. BRASIL. Projeto de Lei n° 2338, de 2023. Autoria: Senador Rodrigo Pacheco (PSD/MG). Disponível em: <https://www25.senado.leg.br/web/atividade/materias/-/materia/157233>. Acesso em: 31 jan. 2025.

5. BRASIL. Autoridade Nacional de Proteção de Dados. Radar Tecnológico: Inteligência Artificial Generativa. Disponível em: <https://www.gov.br/anpd/pt-br/centrais-de-conteudo/documentos-tecnicos-orientativos/radar_tecnologico_ia_generativa_anpd.pdf>. Acesso em: 31 jan. 2025.

6. BRASIL. Tribunal de Contas da União. Guia de uso de inteligência artificial generativa no Tribunal de Contas da União (TCU). Disponível em: <https://portal.tcu.gov.br/data/files/42/F7/91/4B/B59019105E366F09E18818A8/Guia%20de%20uso%20de%20IA%20generativa%20no%20TCU.pdf> .Acesso em: 31 jan. 2025.

7. BRASIL. Controladoria-Geral da União (CGU). Guia de Uso Responsável de Inteligência Artificial. Brasília: CGU, 2024. Disponível em: <https://repositorio.cgu.gov.br/bitstream/1/94244/2/Guia_de_uso_responsavel_de_IA_v5_publicacao.pdf>. Acesso em: 31 jan. 2025.

8. CANADA. Guide on the Use of Generative AI. Disponível em: <https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html>. Acesso em: 31 jan. 2025.

9. CHATTCU – TRIBUNAL DE CONTAS DA UNIÃO. Uso de inteligência artificial aprimora processos internos no TCU. Disponível em: <https://revista.tcu.gov.br/ojs/index.php/RTCU/article/view/2114/1966>    
   <https://portal.tcu.gov.br/imprensa/noticias/uso-de-inteligencia-artificial-aprimora-processos-internos-no-tribunal-de-contas-da-uniao.> Acesso em: 07 out. 2025.

10. ESTADOS UNIDOS. AI Use Case Inventories – Office of Management and Budget / CIO

Disponível em:    
<https://github.com/ombegov/2024-Federal-AI-Use-Case-Inventory>    
[https://www.cio.gov/policies-and-priorities/Executive-Order-13960-AI-Use-Case-Inventories-Reference/.](https://www.cio.gov/policies-and-priorities/Executive-Order-13960-AI-Use-Case-Inventories-Reference/) Acesso em: 07 out. 2025.

11. IA LEGIS – MGI E SERPRO. Ferramenta para facilitar busca por legislação de pessoal   
    Disponível em:  <https://www.gov.br/servidor/pt-br/assuntos/noticias/2025/marco/mgi-e-serpro-lancam-nova-ferramenta-para-facilita-busca-por-legislacao-de-pessoal>       
    <https://legis.sigepe.gov.br/legis/chat-legis.> Acesso em: 07 out. 2025.

12. OCDE - Framework para Classificação de Sistemas de IA. Disponível em:    
    <https://www.oecd.org/en/publications/oecd-framework-for-the-classification-of-ai-systems_cb6d9eca-en.html.> Acesso em: 07 out. 2025.

13. Reino Unido. AI.gov.uk – Knowledge Hub. Disponível em: <https://ai.gov.uk/knowledge-hub/use-cases.> Acesso em: 07 out. 2025.

14. SEI IA – Agência Nacional de Telecomunicações (Anatel)   
    Inteligência artificial no Sistema Eletrônico de Informações. Disponível em:    
    <https://www.gov.br/anatel/pt-br/assuntos/noticias/anatel-inova-com-inteligencia-artificial-no-sistema-eletronico-de-informacoes>    
    Código-fonte: <https://github.com/anatelgovbr/sei-ia.> Acesso em: 07 out. 2025.

15. UNESCO. Recomendação sobre a Ética da Inteligência Artificial. Disponível em:    
    <https://unesdoc.unesco.org/ark:/48223/pf0000381137_por.> Acesso em: 07 out. 2025.

16. UNIÃO EUROPEIA. Public Sector Tech Watch (PSTW). Disponível em:    
    <https://interoperable-europe.ec.europa.eu/collection/public-sector-tech-watch.> Acesso em: 07 out. 2025.

17. UNITED KINGDOM. Guidance to civil servants on use of generative AI. Disponível em: <https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai>. Acesso em: 31 jan. 2025.
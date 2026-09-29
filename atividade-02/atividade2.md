**TAREFA 1**

| Problema identificado                                                       | Possível consequência para o produto ou para a equipe|
| --------------------------------------------------------------------------- | ---------------------------------------------------- |
|Os critérios para considerar uma funcionalidade nem sempre ficam claros, |Uma funcionalidade pode ser liberada sem ter sido suficientemente testada ,ou sem atender aos requisitos esperados, e até ser lançada defeituoso.|
| Alguns integrantes acreditam que somente o QA deve testar.                  | Defeitos podem ser percebidos mais tarde, podendo o produto não ser entrague na data ou entrgue com varios problemas. |
| Defeitos são identificados, mas nem sempre são registrados ou acompanhados. | Problemas podem ser esquecidos, repetidos ou chegar aos usuários sem correção da equipe.|

Não. A qualidade deve ser responsabilidade compartilhada por toda a equipe. O desenvolvedor deve verificar e testar o código produzido, o QA deve planejar e executar testes, e o responsável pelo produto deve ajudar a definir os critérios de aceitação. Dessa forma, problemas podem ser identificados mais cedo e a qualidade é construída durante todo o desenvolvimento, pois se deixarmos apenas para o QA muitos itens podem ser não verificados e podem estar errado.

**TAREFA 2**

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais | 
| ---------- | --------------- | ------------------------------------------ | --------------------- | ---------------------------- |

| João Lucas   | Desenvolvedor | Implementa as funcionalidades conforme os requisitos, cria testes unitários, corrigi defeitos e participa das revisões de código.| Programação, testes unitários, Git, depuração de erros e conhecimento da arquitetura do sistema. | Colaboração, comunicação, organização, atenção aos detalhes e pensamento crítico. |

| João Lucas | Responsável pelo Produto | Defini e esclarece requisitos, estabelece critérios de aceitação, prioriza funcionalidades e defeitos e participa da decisão sobre novas versões. | Levantamento e análise de requisitos, conhecimento do negócio e técnicas de priorização. | Comunicação, organização, negociação, tomada de decisão e colaboração. |

| Pedro Nunes | QA / Analista de Qualidade | Planeja e executa testes, verifica critérios de aceitação, registra defeitos e acompanha suas correções. | Técnicas de teste de software, elaboração de casos de teste, análise de requisitos e ferramentas de gerenciamento de defeitos. | Atenção aos detalhes, comunicação, pensamento crítico, organização e colaboração. |

| Pedro Nunes | DevOps | Automatiza e acompanha processos de integração e implantação, mantem ambientes e apoia a disponibilização segura das versões. | CI/CD, Git, containers, ambientes de implantação, monitoramento e automação. | Organização, comunicação, colaboração, resolução de problemas e responsabilidade. |


**TAREFA 3**

| Atividade de qualidade                | Responsável pelo Produto | Desenvolvedor | QA  | DevOps |
| ------------------------------------- | ------------------------ | ------------- | --- | ----------------- |
| Definir critérios de aceitação        | A/R                      | C             | C   | I                 |
| Revisar requisitos                    | A                        | C             | R   | I                 |
| Implementar a funcionalidade          | I                        | R             | C   | C                 |
| Revisar o código                      | I                        | R             | C   | C                 |
| Criar testes unitários                | I                        | R/A           | C   | I                 |
| Planejar e executar testes do sistema | I                        | C             | R/A | C                 |
| Registrar e acompanhar defeitos       | I                        | C             | R/A | C                 |
| Priorizar a correção dos defeitos     | A/R                      | C             | C   | I                 |
| Aprovar a disponibilização da versão  | A                        | C             | C   | R                 |


## Lacuna ou conflito encontrado

Uma possível lacuna é a aprovação da disponibilização de uma nova versão, pois essa responsabilidade pode ficar indefinida entre o Responsável pelo Produto, QA e DevOps. Sem uma definição clara, uma versão pode ser publicada sem que alguém assuma formalmente a decisão final.

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos|
| ------------------- | ----------------------------- | ---------------- |
| Definir uma Definition of Done para cada funcionalidade.| Ajuda a deixar claros os critérios necessários para considerar uma funcionalidade pronta, evitando entregas incompletas ou com defeitos conhecidos. | Responsável pelo Produto, Desenvolvedor e QA|
| Registrar e acompanhar todos os defeitos encontrados em uma ferramenta ou lista padronizada. | Evita que defeitos sejam esquecidos, facilita o acompanhamento das correções e melhora a comunicação entre a equipe. | QA, Desenvolvedor, Responsável pelo Produto e DevOps |

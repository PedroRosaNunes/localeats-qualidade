**TAREFA 1**

## Objetivo dos testes:
-Verificar se as funcionalidades de login e de favoritar/desfavoritar restaurantes apresentam comportamentos adequados tanto em situações válidas quanto em situações inválidas, reduzindo o risco de acesso incorreto e inconsistências na lista de favoritos.

## Escopo
| Integrante | Funcionalidade incluída | O que será verificado |
| ---------- | ----------------------- | --------------------- |
| João Lucas | Entrar no sistema | Verificar o comportamento do login com credenciais válidas e inválidas. |
| Pedro Nunes | Favoritar e desfavoritar restaurantes | Verificar se um restaurante pode ser adicionado e removido corretamente dos favoritos. |

| Funcionalidade não incluída | Justificativa |
|---|---|
| Fazer pedido | O planejamento foi delimitado às funcionalidades escolhidas pelos dois integrantes da equipe. |

## Abordagem
| Item | Decisão da equipe | Justificativa |
| ---- | ----------------- | ------------- |
| Níveis de teste | Teste de sistema | As funcionalidades serão analisadas pela interface da aplicação, considerando o comportamento completo percebido pelo usuário. |
| Tipos de teste | Funcional | O objetivo é verificar se as funcionalidades apresentam os resultados esperados. |
| Perspectiva caixa-preta ou caixa-branca | Caixa-preta | Serão analisadas entradas e resultados da aplicação sem acesso ao código-fonte. |
| Técnicas de teste | Particionamento de equivalência e transição de estados | O particionamento será utilizado no login e a transição de estados na funcionalidade de favoritos. |

## Ambiente e Responsabilidades
| Item | Definição |
| ---- | --------- |
| Ambiente necessário | Aplicação LocalEats disponível, navegador atualizado, conexão com a internet e conta de usuário de teste. |
| Responsáveis pelo planejamento | João Lucas e Pedro Nunes |
| Responsáveis pela especificação dos casos | Cada integrante será responsável pelos casos relacionados à sua funcionalidade. |
| Responsáveis pela futura execução | João Lucas e Pedro Nunes |

## Critérios
| Critério | Definição da equipe |
| -------- | ------------------- |
| Entrada | Aplicação disponível, conexão com a internet e conta de teste preparada para os casos que exigirem autenticação. |
| Saída | Todos os casos de teste planejados executados futuramente e seus resultados registrados. |
| Suspensão | Aplicação indisponível ou problema no ambiente que impeça a realização dos testes. |

**TAREFA 2**
-JOÃO LUCAS

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---------------------------------------------------------------------------------------------------|
| ID |João Lucas | Entrar no sistema | O sistema permitir acesso utilizando credenciais inválidas. | Uma pessoa poderia acessar o sistema sem fornecer credenciais válidas, comprometendo o controle de acesso e segurança da conta. | Baixa | Alta | Alta | Mesmo que a ocorrência não seja frequente, permitir acesso indevido teria consequência grave para o sistema e para os usuários, edanificando sua reputação . |

 | Classe   | Situação                                               | Resultado esperado  |
| -------- | ------------------------------------------------------ | ------------------- |
| Válida   | E-mail e senha correspondentes a um usuário cadastrado | Permitir acesso     |
| Inválida | E-mail válido com senha incorreta                      | Não permitir acesso |
| Inválida | Credenciais não correspondentes a uma conta válida     | Não permitir acesso |

## No trabalho:

- Integrante responsável: João Lucas
- Funcionalidade: Entrar no sistema
- Risco relacionado: R01
- Técnica escolhida: Particionamento de equivalência

## Por que a técnica foi escolhida?

- O particionamento de equivalência foi escolhido porque as entradas do login podem ser divididas em grupos de credenciais válidas e inválidas. Dessa forma, é possível selecionar casos representativos sem testar todas as combinações possíveis de e-mail e senha.

## Aplicação da técnica

- Foram definidas uma classe válida, contendo credenciais correspondentes a um usuário cadastrado, e classes inválidas, contendo credenciais que não permitem autenticação.

## Casos derivados

- CT01 e CT02.

-PEDRO NUNES

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|------------------------------------------------------------------------------------------------|
| R02 | Pedro Nunes | Favoritar e desfavoritar restaurantes | O estado de favorito não ser atualizado corretamente após a ação do usuário. | O usuário pode não conseguir identificar corretamente quais restaurantes estão salvos como favoritos. | Média | Média | Média | O problema prejudica a organização dos restaurantes escolhidos pelo usuário, embora não impeça o uso do aplicavo. |

## No trabalho:

- Integrante responsável: Pedro Nunes
- Funcionalidade: Favoritar e desfavoritar restaurantes
- Risco relacionado: R02
- Técnica escolhida: Transição de estados

## Por que a técnica foi escolhida?

- A técnica foi escolhida porque a funcionalidade possui estados claramente diferentes. Um restaurante pode estar não favoritado ou favoritado, e as ações do usuário devem provocar corretamente a mudança entre esses estados.

| Estado inicial | Ação         | Estado esperado |
| -------------- | ------------ | --------------- |
| Não favoritado | Favoritar    | Favoritado      |
| Favoritado     | Desfavoritar | Não favoritado  |

## Casos derivados

- CT03 e CT04.

**TAREFA 3**

## CT01 — Realizar login com credenciais válidas

Integrante responsável: João Lucas  
Funcionalidade: Entrar no sistema  
Risco relacionado: R01  
Técnica utilizada: Particionamento de equivalência

Pré-condição:
Existir uma conta de teste cadastrada no LocalEats.

Dados de entrada:
E-mail válido de teste e senha válida correspondente.

Passos:
1. Acessar a tela de login.
2. Informar o e-mail válido.
3. Informar a senha válida.
4. Confirmar o login.

Resultado esperado:
O sistema deve permitir o acesso do usuário à aplicação.

### CT02: Tentar fazer login com senha inválida

Integrante responsável: João Lucas  
Funcionalidade: Entrar no sistema  
Risco relacionado: R01  
Técnica utilizada: Particionamento de equivalência

Pré-condição:
Existir uma conta de teste cadastrada no LocalEats.

Dados de entrada:
E-mail válido de teste e senha diferente da senha cadastrada.

Passos:
1. Acessar a tela de login.
2. Informar o e-mail válido.
3. Informar uma senha inválida.
4. Confirmar o login.

Resultado esperado:
O sistema não deve permitir o acesso utilizando as credenciais inválidas.

### CT03: Adicionar restaurante aos favoritos

Integrante responsável: Pedro Nunes  
Funcionalidade: Favoritar e desfavoritar restaurantes  
Risco relacionado: R02  
Técnica utilizada: Transição de estados

Pré-condição:
O usuário está autenticado e o restaurante escolhido não está marcado como favorito.

Dados de entrada:
Um restaurante disponível na aplicação.

Passos:
1. Acessar a lista de restaurantes.
2. Selecionar um restaurante que não esteja favoritado.
3. Utilizar a opção de favoritar.

Resultado esperado:
O restaurante deve passar do estado não favoritado para favoritado e ser identificado pelo sistema como favorito.

### CT04: Remover restaurante dos favoritos

Integrante responsável: Pedro Nunes  
Funcionalidade: Favoritar e desfavoritar restaurantes  
Risco relacionado: R02  
Técnica utilizada: Transição de estados

Pré-condição:
O usuário está autenticado e o restaurante escolhido está marcado como favorito.

Dados de entrada:
Um restaurante previamente favoritado.

Passos:
1. Acessar os restaurantes favoritos.
2. Selecionar um restaurante favoritado.
3. Utilizar a opção de desfavoritar.

Resultado esperado:
O restaurante deve passar do estado favoritado para não favoritado e deixar de ser identificado como favorito.

## Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| João Lucas | Entrar no sistema | R01: acesso com credenciais inválidas | Particionamento de equivalência | CT01 e CT02 |
| Pedro Nunes | Favoritar e desfavoritar restaurantes | R02: estado de favorito atualizado incorretamente | Transição de estados | CT03 e CT04 |
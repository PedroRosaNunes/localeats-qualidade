# Atividade 4: Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software
**Projeto:** LocalEats (https://local-eats-unisenac.vercel.app/)
**Equipe (dupla):** Pedro Nunes e João Lucas Nunes

| Integrante | Regra unitária | Fluxo funcional (Playwright) |
|---|---|---|
| Pedro Nunes | Regra 1: `pedido_atingiu_valor_minimo` | Pesquisar um restaurante |
| João Lucas Nunes | Regra 2: `calcular_desconto` | Selecionar uma categoria |

## Como executar

```powershell
pip install -r requirements.txt
python -m playwright install
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

## Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Pedro Nunes | Unitário | Pedido de R$ 30,00 atinge o valor mínimo | tests/test_regras_localeats.py::test_pedido_atinge_valor_minimo |
| TU02 | Pedro Nunes | Unitário | Pedido de R$ 20,00 fica abaixo do mínimo | tests/test_regras_localeats.py::test_pedido_abaixo_do_valor_minimo |
| TU03 | João Lucas Nunes | Unitário | Pedido de R$ 150,00 recebe desconto de 10% | tests/test_regras_localeats.py::test_pedido_de_150_recebe_desconto_de_10_por_cento |
| TU04 | João Lucas Nunes | Unitário | Pedido de R$ 99,99 não recebe desconto | tests/test_regras_localeats.py::test_pedido_abaixo_de_100_nao_recebe_desconto |
| TF01 | Pedro Nunes | Funcional | Pesquisa de restaurantes pela localização "Zona Norte" no LocalEats | tests/test_localeats.py::test_pesquisar_restaurante_por_localizacao |
| TF02 | João Lucas Nunes | Funcional | Seleção da categoria Italiana e retorno para Todos | tests/test_localeats.py::test_selecionar_categoria_italiana |

## Parte 1: Testes unitários e TDD

### TDD de Pedro Nunes

- **Regra escolhida:** Regra 1, `pedido_atingiu_valor_minimo(valor_pedido)`.
- **Primeiro teste escrito:** `test_pedido_atinge_valor_minimo`, que verifica se um pedido de R$ 30,00 retorna `True`.
- **Por que o teste falhou inicialmente:** a função ainda não existia; o pytest acusou `ModuleNotFoundError: No module named 'src.regras_localeats'`.
- **Implementação mínima realizada:** criação do arquivo `src/regras_localeats.py` com a função retornando `valor_pedido >= 30`.
- **Segundo teste escrito:** `test_pedido_abaixo_do_valor_minimo`, que verifica se um pedido de R$ 20,00 retorna `False`.
- **Melhoria ou refatoração realizada:** o valor 30 foi movido para a constante `VALOR_MINIMO_PEDIDO` e foi adicionada a validação que lança `ValueError` para valores negativos, conforme a regra.

### TDD de João Lucas Nunes

- **Regra escolhida:** Regra 2, `calcular_desconto(valor_pedido)`.
- **Primeiro teste escrito:** `test_pedido_de_150_recebe_desconto_de_10_por_cento`, que verifica se um pedido de R$ 150,00 retorna desconto de 15.
- **Por que o teste falhou inicialmente:** a função `calcular_desconto` ainda não existia; o pytest acusou `ModuleNotFoundError: No module named 'src.regras_localeats'`.
- **Implementação mínima realizada:** função retornando `valor_pedido * 10 / 100` para qualquer valor.
- **Segundo teste escrito:** `test_pedido_abaixo_de_100_nao_recebe_desconto`, que verifica se R$ 99,99 retorna 0 (limite logo abaixo de R$ 100,00).
- **Melhoria ou refatoração realizada:** inclusão da condição `valor_pedido >= 100` para aplicar o desconto só a partir de R$ 100,00, criação das constantes `VALOR_PARA_DESCONTO` e `PERCENTUAL_DESCONTO` e validação de `ValueError` para valores negativos.

## Parte 2: Testes funcionais com Playwright

Ao acessar o LocalEats sem sessão, o sistema redireciona para a tela de login. Por isso, antes de cada teste funcional, uma fixture (`pagina_logada`) cria uma conta com e-mail único pela aba **Criar Conta** e deixa o usuário logado. Em seguida, os testes acessam `https://local-eats-unisenac.vercel.app/`, esperam o texto "Carregando os melhores restaurantes" desaparecer e usam locators do Playwright.

### TF01: Pesquisar um restaurante (Pedro Nunes)

1. Abre a página inicial e espera os restaurantes carregarem (cada restaurante é um link para `restaurant.html?id=N`).
2. Digita "Zona Norte" no campo de busca e clica em **Buscar**.
3. Observação da exploração: apesar de o campo indicar "Buscar por culinária ou localização...", ao pesquisar por culinária (ex.: "Mexicana") nenhum restaurante foi retornado; a busca só funcionou por localização.
4. Assertions: o campo contém o texto digitado; todos os restaurantes exibidos são da "Zona Norte"; há pelo menos 1 resultado e menos que a lista completa.

### TF02: Selecionar uma categoria (João Lucas Nunes)

1. Abre a página inicial e espera os restaurantes carregarem.
2. Clica no botão da categoria **Italiana**.
3. Clica novamente em **Todos**.
4. Assertions: com a categoria Italiana nenhum restaurante exibido é de outra culinária e há pelo menos 1 resultado e menos que o total; ao voltar para **Todos**, a quantidade de restaurantes volta a ser igual ao total inicial.

## Relatório da execução

O arquivo está no mesmo diretório e foi gerado com:

```
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

## Uso de inteligência artificial

- **Ferramenta utilizada:** Claude (Anthropic).
- **Como a ferramenta foi utilizada:** apoio para estruturar a estrutura do relatorio.
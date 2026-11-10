import re
import uuid

import pytest
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError

URL = "https://local-eats-unisenac.vercel.app/"
URL_LOGIN = URL + "static/login.html"
TEXTO_CARREGANDO = "Carregando os melhores restaurantes..."
SENHA_TESTE = "Senha@12345"


def autenticar(page: Page):
    """Cria uma conta com e-mail único e garante que o usuário fique logado."""
    email = f"teste.{uuid.uuid4().hex[:8]}@teste.com"

    page.goto(URL_LOGIN)
    page.get_by_role("button", name="Criar Conta").click()

    formulario = page.locator("form").filter(has_text="Registrar")
    campos = formulario.locator("input")
    campos.nth(0).fill("Teste Automatizado")
    campos.nth(1).fill(email)
    campos.nth(2).fill(SENHA_TESTE)
    formulario.get_by_role("button", name="Registrar").click()

    try:
        # Se o sistema já entrar sozinho após registrar, vai para a página inicial
        page.wait_for_url(re.compile(r"index\.html"), timeout=5000)
    except PlaywrightTimeoutError:
        # Caso contrário, faz o login com a conta recém-criada
        page.get_by_role("button", name="Entrar").first.click()
        campos_login = page.locator("form:visible").locator("input")
        campos_login.nth(0).fill(email)
        campos_login.nth(1).fill(SENHA_TESTE)
        page.get_by_role("button", name="Entrar").last.click()
        page.wait_for_url(re.compile(r"index\.html"))


@pytest.fixture
def pagina_logada(page: Page) -> Page:
    autenticar(page)
    return page


def abrir_localeats(page: Page):
    """Acessa o LocalEats e espera a lista de restaurantes terminar de carregar."""
    page.goto(URL)
    expect(page.get_by_text(TEXTO_CARREGANDO)).to_be_hidden(timeout=15000)
    expect(cards_de_restaurantes(page).first).to_be_visible()


def cards_de_restaurantes(page: Page):
    """Cada restaurante é um link para restaurant.html?id=N."""
    return page.locator("a[href*='restaurant.html']")


# Responsável: Pedro Nunes
def test_pesquisar_restaurante_por_localizacao(pagina_logada: Page):
    page = pagina_logada
    abrir_localeats(page)
    cards = cards_de_restaurantes(page)
    total = cards.count()

    campo_busca = page.get_by_role("textbox")
    campo_busca.fill("Zona Norte")
    page.get_by_role("button", name="Buscar").click()

    expect(cards.first).to_be_visible()
    expect(campo_busca).to_have_value("Zona Norte")
    expect(cards.filter(has_not_text="Zona Norte")).to_have_count(0)
    assert 1 <= cards.count() < total


# Responsável: João Lucas Nunes
def test_selecionar_categoria_italiana(pagina_logada: Page):
    page = pagina_logada
    abrir_localeats(page)
    cards = cards_de_restaurantes(page)
    total = cards.count()

    page.get_by_role("button", name="Italiana", exact=True).click()
    page.wait_for_load_state("networkidle")

    expect(cards.filter(has_not_text="Italiana")).to_have_count(0)
    assert 1 <= cards.count() < total

    page.get_by_role("button", name="Todos", exact=True).click()
    expect(cards).to_have_count(total)
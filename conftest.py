import pytest
from paginas.cliente_conta_page import ClienteContaPage
from paginas.cliente_login_page import ClienteLoginPage
from paginas.gerente_page import GerentePage
from paginas.login_page import LoginPage

def pytest_addoption(parser):
    """
    Configurações do pytest para aceitar opções de linha de comando.
    """
    parser.addoption("--navegador", action="store", default="chrome", help="Escolha o navegador: chrome, firefox ou edge.")

@pytest.fixture
def abrir_pagina_inicial(request):
    """
    Configurações para abrir pagina inicial.
    """
    navegador_selecionado = request.config.getoption('navegador').lower()
    login_page = LoginPage(browser=navegador_selecionado)
    login_page.abrir_pagina()
    yield login_page
    login_page.fechar_pagina()

@pytest.fixture
def abrir_pagina_conta_cliente(abrir_pagina_inicial):
    """
    Configurações para abrir a página da conta do cliente.
    """
    if abrir_pagina_inicial.checar_url_login():
        abrir_pagina_inicial.clicar_botao_cliente_login()

    cliente_login_page = ClienteLoginPage(abrir_pagina_inicial.driver)
    cliente_login_page.selecionar_cliente()
    cliente_login_page.clicar_botao_login()

    cliente_conta_page = ClienteContaPage(cliente_login_page.driver)

    yield  cliente_conta_page

@pytest.fixture
def abrir_pagina_gerente(abrir_pagina_inicial):
    """
    Configurações para abrir a página do gerente.
    """
    if abrir_pagina_inicial.checar_url_login():
        abrir_pagina_inicial.clicar_botao_gerente_login()

    gerente_page = GerentePage(abrir_pagina_inicial.driver)

    yield  gerente_page

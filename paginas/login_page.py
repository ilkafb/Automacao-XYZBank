from selenium.webdriver.common.by import By
from paginas.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(BasePage):
    """
    Classe que representa a página de login.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    botao_login_cliente = (By.XPATH, "//button[text()='Customer Login']")
    botao_login_gerente = (By.XPATH, "//button[text()='Bank Manager Login']")

    def __init__(self, browser):
        """
        Inicializa a classe com o navegador.
        """
        super().__init__(driver=None, browser=browser)

    def abrir_pagina(self):
        """
        Abrir o navegador.
        """
        self.driver.get(self.url)

    def checar_url_login(self):
        """
        Verifica se a URL atual é igual a da página.
        """
        return self.checar_url(self.url)

    def clicar_botao_cliente_login(self):
        """
        Navega para página do login do cliente.
        """
        self.clicar_botao(self.botao_login_cliente)

    def clicar_botao_gerente_login(self):
        """
        Navega para página do login do gerente.
        """
        self.clicar_botao(self.botao_login_gerente)

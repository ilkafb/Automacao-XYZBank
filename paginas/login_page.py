from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(BasePage):
    """
    Classe que representa a página de login.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    botao_login = (By.XPATH, "//button[text()='Customer Login']")

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
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(self.botao_login)
        )
        self.driver.find_element(*self.botao_login).click()

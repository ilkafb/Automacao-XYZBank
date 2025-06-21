from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ClienteLoginPage(BasePage):
    """
    Classe que representa a página de login do cliente.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'
    select_cliente = (By.ID, "userSelect")
    botao_login = (By.CLASS_NAME, "btn.btn-default")

    def __init__(self, driver):
        """
        Inicializa a classe com o driver.
        """
        super().__init__(driver)

    def checar_url_cliente_login(self):
        """
        Verifica se a URL atual é igual a da página.
        """
        return self.checar_url(self.url)

    def selecionar_cliente(self):
        """
        Seleciona o cliente para realizar o login.
        """
        select_element = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.select_cliente))
        select = Select (select_element)
        select.select_by_value("1")

    def clicar_botao_login(self):
        """
        Navega para página da conta do cliente.
        """
        self.clicar_botao(self.botao_login)

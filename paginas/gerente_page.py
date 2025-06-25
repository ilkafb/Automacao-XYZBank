from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from paginas.base_page import BasePage


class GerentePage(BasePage):
    """
    Classe que representa a página do gerente.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    botao_adicionar_cliente = (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
    campo_primeiro_nome = (By.CSS_SELECTOR, '[ng-model="fName"]')
    campo_ultimo_nome = (By.CSS_SELECTOR, '[ng-model="lName"]')
    campo_codigo_postal = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    botao_formulario = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        """
        Inicializa a classe com o driver.
        """
        super().__init__(driver)

    def checar_url_gerente(self):
        """
        Verifica se a URL atual é igual a da página.
        """
        return self.checar_url(self.url)

    def clicar_botao_adicionar_cliente(self):
        """
        Exibe os campos para criar um novo cliente.
        """
        self.clicar_botao(self.botao_adicionar_cliente)

    def preencher_campos_adicionar_cliente(self, primeiro_nome, ultimo_nome, codigo_postal):
        """
        Preenche os campos de valor com o dado informado.
        """
        self.preencher_campo(self.campo_primeiro_nome, primeiro_nome)
        self.preencher_campo(self.campo_ultimo_nome, ultimo_nome)
        self.preencher_campo(self.campo_codigo_postal, codigo_postal)

    def clicar_botao_enviar_formulario(self):
        """
        Clica no botão para submeter o formulário de depósito.
        """
        self.clicar_botao(self.botao_formulario)

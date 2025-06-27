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
    botao_clientes = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    campo_primeiro_nome = (By.CSS_SELECTOR, '[ng-model="fName"]')
    campo_ultimo_nome = (By.CSS_SELECTOR, '[ng-model="lName"]')
    campo_codigo_postal = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    botao_formulario = (By.CSS_SELECTOR, '[type="submit"]')
    tabela_clientes = (By.TAG_NAME, 'table')
    campo_pesquisar_cliente = (By.CSS_SELECTOR, '[ng-model="searchCustomer"]')

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

    def clicar_botao_clientes(self):
        """
        Exibe a tela de lista dos clientes.
        """
        self.clicar_botao(self.botao_clientes)

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

    def verificar_cabecalho_tabela_clientes(self):
        """
        Verifica o cabeçalho da tabela clientes.
        """
        return self.verificar_cabecalho_tabela(self.tabela_clientes, ["First Name", "Last Name", "Post Code", "Account Number", "Delete Customer"])

    def verificar_linhas_tabela_clientes(self):
        """
        Verifica as linhas da tabela clientes.
        """
        return self.verificar_linhas_tabela(self.tabela_clientes, [
        ["Hermoine", "Granger", "E859AB", ["1001", "1002", "1003"]],
        ["Harry", "Potter", "E725JB", ["1004", "1005", "1006"]],
        ["Ron", "Weasly", "E55555", ["1007", "1008", "1009"]],
        ["Albus", "Dumbledore", "E55656", ["1010", "1011", "1012"]],
        ["Neville", "Longbottom", "E89898", ["1013", "1014", "1015"]],
        ])

    def pesquisar_cliente(self, nome_cliente):
        """
        Preenche o campo de pesquisa para filtrar a lista de clientes.
        """
        self.preencher_campo(self.campo_pesquisar_cliente, nome_cliente)
        
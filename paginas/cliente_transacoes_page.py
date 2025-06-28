from selenium.webdriver.common.by import By
from paginas.base_page import BasePage

class ClienteTransacoesPage(BasePage):
    """
    Classe que representa a página do histórico de transações do cliente.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx'
    botao_reset = (By.CSS_SELECTOR, "[ng-click='reset()']")
    tabela_clientes = (By.TAG_NAME, 'table')

    def __init__(self, driver):
        """
        Inicializa a classe com o driver.
        """
        super().__init__(driver)

    def checar_url_cliente_transacoes(self):
        """
        Verifica se a URL atual é igual a da página.
        """
        return self.checar_url(self.url)

    def clicar_botao_reset(self):
        """
        Clica no botão para resetar o histórico de transações.
        """
        self.clicar_botao(self.botao_reset)

    def verificar_cabecalho_tabela_transacoes(self):
        """
        Verifica o cabeçalho da tabela transacoes.
        """
        return self.verificar_cabecalho_tabela(self.tabela_transacoes, ["Date-Time", "Amount", "Transaction Type"])

    def obter_quantidade_transacoes(self):
        """
        Obtém a quantidade de transações na tabela.
        """
        return self.obter_quantidade_linhas_tabela(self.tabela_clientes)

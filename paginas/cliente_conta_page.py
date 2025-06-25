from selenium.webdriver.common.by import By
from paginas.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

class ClienteContaPage(BasePage):
    """
    Classe que representa a página de conta do cliente.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'
    botao_deposito = (By.CSS_SELECTOR, '[ng-class="btnClass2"]')
    botao_saque = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    div_informacoes = (By.CSS_SELECTOR, 'div.center')
    campo_formulario = (By.CSS_SELECTOR, 'input')
    botao_formulario = (By.CSS_SELECTOR, '[type="submit"]')
    span_mensagem_aviso =  (By.CSS_SELECTOR, 'span.error')
    select_conta = (By.ID, "accountSelect")

    def __init__(self, driver):
        """
        Inicializa a classe com o driver.
        """
        super().__init__(driver)

    def checar_url_cliente_conta(self):
        """
        Verifica se a URL atual é igual a da página.
        """
        return self.checar_url(self.url)

    def obter_informacoes(self):
        """
        Obtém e retorna as informações da conta do cliente (número, saldo e moeda).
        """
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.div_informacoes)
        )
        informacoes = self.driver.find_element(*self.div_informacoes).text
        partes = informacoes.split(" , ")
        numero_conta = int(partes[0].split(" : ")[1])
        valor_conta = float(partes[1].split(" : ")[1])
        moeda_conta = partes[2].split(" : ")[1]
        return numero_conta, valor_conta, moeda_conta

    def clicar_botao_deposito(self):
        """
        Exibe o campo para informar o valor do depósito.
        """
        self.clicar_botao(self.botao_deposito)

    def clicar_botao_saque(self):
        """
        Exibe o campo para informar o valor do saque.
        """
        self.clicar_botao(self.botao_saque)

    def preencher_campo_valor(self, valor):
        """
        Preenche o campo de valor com o dado informado.
        """
        self.preencher_campo(self.campo_formulario, valor)

    def clicar_botao_enviar_formulario(self):
        """
        Clica no botão para submeter o formulário de depósito.
        """
        self.clicar_botao(self.botao_formulario)

    def clicar_botao_alterar_conta(self, numero_conta):
        """
        Clica no botão para alterar a conta do cliente.
        """
        select_element = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.select_conta))
        select = Select(select_element)
        select.select_by_value(f'number:{numero_conta}')

    def mensagem_visivel(self):
        """
        Verifica se a mensagem de aviso está visível na tela.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(self.span_mensagem_aviso)
            )
            return True
        except Exception:
            return False

    def checar_mensagem(self, mensagem):
        """
        Verifica se a mensagem exibida é igual à esperada.
        """
        if self.mensagem_visivel():
            return mensagem == self.driver.find_element(*self.span_mensagem_aviso).text

        return False



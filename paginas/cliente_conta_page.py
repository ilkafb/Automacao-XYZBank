from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(self.botao_deposito)
        )
        self.driver.find_element(*self.botao_deposito).click()

    def clicar_botao_saque(self):
        """
        Exibe o campo para informar o valor do saque.
        """
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(self.botao_saque)
        )
        self.driver.find_element(*self.botao_saque).click()

    def preencher_campo(self, valor):
        """
        Preenche o campo de valor com o dado informado.
        """
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.campo_formulario)
        )
        self.driver.find_element(*self.campo_formulario).send_keys(valor)

    def clicar_botao_enviar_formulario(self):
        """
        Clica no botão para submeter o formulário de depósito.
        """
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(self.botao_formulario)
        )
        self.driver.find_element(*self.botao_formulario).click()

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



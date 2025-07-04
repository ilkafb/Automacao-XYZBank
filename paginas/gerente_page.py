from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from paginas.base_page import BasePage
from selenium.webdriver.support.ui import Select

class GerentePage(BasePage):
    """
    Classe que representa a página do gerente.
    """
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    botao_adicionar_cliente = (By.CSS_SELECTOR, '[ng-class="btnClass1"]')
    botao_abrir_conta_cliente = (By.CSS_SELECTOR, '[ng-class="btnClass2"]')
    botao_clientes = (By.CSS_SELECTOR, '[ng-class="btnClass3"]')
    campo_primeiro_nome = (By.CSS_SELECTOR, '[ng-model="fName"]')
    campo_ultimo_nome = (By.CSS_SELECTOR, '[ng-model="lName"]')
    campo_codigo_postal = (By.CSS_SELECTOR, '[ng-model="postCd"]')
    botao_formulario = (By.CSS_SELECTOR, '[type="submit"]')
    tabela_clientes = (By.TAG_NAME, 'table')
    campo_pesquisar_cliente = (By.CSS_SELECTOR, '[ng-model="searchCustomer"]')
    botao_deletar_cliente = (By.TAG_NAME, 'button')
    select_cliente = (By.ID, "userSelect")
    select_moeda = (By.ID, "currency")

    lista_clientes = [
        ["Hermoine", "Granger", "E859AB", ["1001", "1002", "1003"]],
        ["Harry", "Potter", "E725JB", ["1004", "1005", "1006"]],
        ["Ron", "Weasly", "E55555", ["1007", "1008", "1009"]],
        ["Albus", "Dumbledore", "E55656", ["1010", "1011", "1012"]],
        ["Neville", "Longbottom", "E89898", ["1013", "1014", "1015"]],
    ]

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
    
    def clicar_botao_abrir_conta_cliente(self):
        """
        Exibe os campos para criar uma conta para um cliente.
        """
        self.clicar_botao(self.botao_abrir_conta_cliente)

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

    def abrir_conta_primeiro_cliente(self):
        """
        Abre uma conta para o primeiro cliente da lista.
        """
        select_cliente = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.select_cliente))
        select_moeda = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.select_moeda))
        
        selects = [Select(select_cliente), Select(select_moeda)]

        for select in selects:
            select.select_by_visible_text(select.options[1].text)

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
        return self.verificar_linhas_tabela(self.tabela_clientes, self.lista_clientes)

    def verificar_cliente(self, primeiro_nome, ultimo_nome, codigo_postal):
        """
        Verifica se o cliente está na tabela de clientes.
        """
        ultima_linha = self.obter_ultima_linha_tabela(self.tabela_clientes)
        if ultima_linha:
            celulas = ultima_linha.find_elements(By.TAG_NAME, 'td')
            if len(celulas) == 5:
                return (primeiro_nome in celulas[0].text and
                        ultimo_nome in celulas[1].text and
                        codigo_postal in celulas[2].text)
        return False

    def verificar_conta_primeiro_cliente(self, numero_conta):
        """
        Verifica se a conta do primeiro cliente corresponde ao número fornecido.
        """
        primeira_linha = self.obter_primeira_linha_tabela(self.tabela_clientes)
        if primeira_linha:
            celulas = primeira_linha.find_elements(By.TAG_NAME, 'td')
            if len(celulas) == 5:
                return numero_conta in self.obter_numeros_contas(celulas[3].text)
        return False

    def pesquisar_cliente(self, nome_cliente):
        """
        Preenche o campo de pesquisa para filtrar a lista de clientes.
        """
        self.preencher_campo(self.campo_pesquisar_cliente, nome_cliente)
        
    def deletar_primeiro_cliente(self):
        """
        Deleta o primeiro cliente da lista.
        """ 
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.tabela_clientes))

        primeira_linha_tabela_antes_delecao = self.obter_primeira_linha_tabela(self.tabela_clientes)
        if primeira_linha_tabela_antes_delecao:
            botao_deletar = primeira_linha_tabela_antes_delecao.find_element(*self.botao_deletar_cliente)

            self.clicar_botao(botao_deletar)
        else:
            raise Exception("Nenhum cliente encontrado na tabela.")
        
    def primeiro_cliente_deletado(self):
        """
        Verifica se o primeiro cliente foi deletado.
        """
        lista_clientes_esperada = self.lista_clientes[1:]
        return self.verificar_linhas_tabela(self.tabela_clientes, lista_clientes_esperada)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    """
    Classe base para páginas.
    """
    def __init__(self, driver, browser=None):
        """
        Inicializa a classe com a URL inicial e configura o navegador Chrome na navegação anônima.
        """
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                options = Options()
                options.add_argument("--incognito")
                # options.add_argument("--headless")
                self.driver = webdriver.Chrome(options=options)
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')

    def fechar_pagina(self):
        """
        Fecha o navegador.
        """
        self.driver.quit()
    def checar_url(self,url):
        """
        Verifica se a URL atual é igual a da página.
        """
        return self.driver.current_url == url

    def preencher_campo(self, campo, valor):
        """
        Preenche um campo com o valor fornecido, usando o localizador.
        Se o valor não for fornecido (None), o campo não será preenchido.
        """
        WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(campo)
        )
        self.driver.find_element(*campo).send_keys(valor)

    def clicar_botao(self, botao):
        """
        Clicar em um botao
        """
        WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(botao)
        )
        if isinstance(botao, WebElement):
            botao.click()
        else:
            self.driver.find_element(*botao).click()

    def obter_mensagem_alerta(self):
        """
        Obter a mensagem de alerta
        """
        return WebDriverWait(self.driver, 5).until(ec.alert_is_present()).text
    
    def fechar_mensagem_alerta(self):
        """
        Fecha a mensagem de alerta
        """
        alerta = WebDriverWait(self.driver, 5).until(ec.alert_is_present())
        alerta.accept()

    def _buscar_elemento(self, seletor):
        """
        Obter um elemento pelo seu seletor
        """
        return WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located(seletor)
        )
    
    def _obter_linhas_conteudo_tabela(self, seletor_tabela):
        """
        Obter as linhas de conteúdo de uma tabela
        """
        minha_tabela = self._buscar_elemento(seletor_tabela)
        minha_tabela_tbody = minha_tabela.find_element(By.TAG_NAME, 'tbody')
        minha_tabela_linhas = minha_tabela_tbody.find_elements(By.TAG_NAME, 'tr')
        return minha_tabela_linhas
    
    def _obter_linha_tabela(self, seletor_tabela, numero_linha):
        """
        Obter uma linha específica de uma tabela
        """
        minha_tabela_linhas = self._obter_linhas_conteudo_tabela(seletor_tabela)
        total_linhas = len(minha_tabela_linhas)

        if not (-total_linhas <= numero_linha < total_linhas):
            raise IndexError("Índice de linha fora do intervalo da tabela.")

        return minha_tabela_linhas[numero_linha]
    
    def obter_primeira_linha_tabela(self, seletor_tabela):
        """
        Obter a primeira linha de uma tabela
        """
        return self._obter_linha_tabela(seletor_tabela, 0)
    
    def obter_ultima_linha_tabela(self, seletor_tabela):
        """
        Obter a última linha de uma tabela
        """
        return self._obter_linha_tabela(seletor_tabela, -1)

    def obter_numeros_contas(self, texto_linha_dados_contas):
        """
        Obter os números de contas de uma tabela
        """
        return [int(n) for n in texto_linha_dados_contas.split(" ")] if texto_linha_dados_contas else []

    def verificar_cabecalho_tabela(self, seletor_tabela, cabecalhos):
        """
        Verificar se o cabeçalho corresponde com o esperado
        """
        minha_tabela = self._buscar_elemento(seletor_tabela)
        minha_tabela_thead = minha_tabela.find_element(By.TAG_NAME, 'thead')
        minha_tabela_cabecalhos = minha_tabela_thead.find_elements(By.TAG_NAME, 'td')
        if len(cabecalhos) != len(minha_tabela_cabecalhos):
            return False
        
        for i, cabecalho_esperado in enumerate(cabecalhos):
            cabecalho_real = minha_tabela_cabecalhos[i].text.strip()
            if cabecalho_esperado != cabecalho_real:
                return False
        return True
    
    def obter_quantidade_linhas_tabela(self, seletor_tabela):
        """
        Obtém a quantidade de linhas de uma tabela
        """
        minha_tabela_linhas = self._obter_linhas_conteudo_tabela(seletor_tabela)
        return len(minha_tabela_linhas)

    def verificar_linhas_tabela(self, seletor_tabela, linhas):
        """
        Verificar se as linhas correspondem com o esperado
        """
        minha_tabela_linhas = self._obter_linhas_conteudo_tabela(seletor_tabela)
        if len(linhas) != len(minha_tabela_linhas):
            return False

        for i, linha_esperada in enumerate(linhas):
            celulas_web = minha_tabela_linhas[i].find_elements(By.TAG_NAME, 'td')
            
            textos_celulas_web = [celulas_web[0].text, celulas_web[1].text, celulas_web[2].text]
            
            if textos_celulas_web != linha_esperada[:3]:
                return False

            numeros_conta_esperados = linha_esperada[3]
            numeros_conta_reais_texto = celulas_web[3].text
            
            if not all(num in numeros_conta_reais_texto for num in numeros_conta_esperados):
                return False

        return True

    def esperar_pelo_numero_de_linhas_da_tabela(self, seletor_tabela, numero_esperado):
        """
        Espera explícita até que uma tabela tenha um número específico de linhas.
        """
        wait = WebDriverWait(self.driver, 5) 
        try:
            wait.until(lambda driver: 
                len(driver.find_element(*seletor_tabela).find_elements(By.CSS_SELECTOR, 'tbody tr')) == numero_esperado
            )
        except:
            raise TimeoutError(f"A tabela não atingiu o número de {numero_esperado} linhas no tempo esperado.")

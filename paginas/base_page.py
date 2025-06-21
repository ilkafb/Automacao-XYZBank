from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
        self.driver.find_element(*botao).click()

    def obter_mensagem_alerta(self):
        """
        Obter a mensagem de alerta
        """
        return WebDriverWait(self.driver, 5).until(ec.alert_is_present()).text

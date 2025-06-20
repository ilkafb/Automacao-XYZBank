from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
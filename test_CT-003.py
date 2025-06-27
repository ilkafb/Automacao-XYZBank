class TestCT003:
    """
    Classe de teste para visualizar lista de clientes.
    """

    def test_visualizar_cliente(self, abrir_pagina_gerente):
        """
        Testa a visualização da lista da tela dos clientes.
        """
        abrir_pagina_gerente.clicar_botao_clientes()
        assert abrir_pagina_gerente.verificar_cabecalho_tabela_clientes(), 'A quantidade de elementos no cabeçalho da tabela é diferente do esperado'
        assert abrir_pagina_gerente.verificar_linhas_tabela_clientes(), 'A quantidade de elementos das linhas da tabela é diferente do esperado'

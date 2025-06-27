class TestCT006:
    """
    Classe de teste para a funcionalidade de pesquisa por um cliente inexistente.
    """

    def test_pesquisar_cliente_inexistente(self, abrir_pagina_gerente):
        """
        Testa a busca por um cliente que não existe e valida se a tabela de resultados fica vazia.
        """
        abrir_pagina_gerente.clicar_botao_clientes()

        abrir_pagina_gerente.pesquisar_cliente("Frodo")

        abrir_pagina_gerente.esperar_pelo_numero_de_linhas_da_tabela(
            abrir_pagina_gerente.tabela_clientes, 0
        )

        dados_esperados = []
        
        assert abrir_pagina_gerente.verificar_linhas_tabela(
            abrir_pagina_gerente.tabela_clientes, dados_esperados 
        ), "A tabela não está vazia após pesquisar por um cliente inexistente."

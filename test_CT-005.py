class TestCT005:
    """
    Classe de teste para a funcionalidade de pesquisa de clientes existente.
    """

    def test_pesquisar_cliente_por_nome(self, abrir_pagina_gerente):
        """
        Testa a busca de um cliente pelo primeiro nome e valida o resultado.
        """
        abrir_pagina_gerente.clicar_botao_clientes()

        abrir_pagina_gerente.pesquisar_cliente("Harry")
        
        dados_esperados_harry = [
            ["Harry", "Potter", "E725JB", ["1004", "1005", "1006"]]
        ]
        
        assert abrir_pagina_gerente.verificar_linhas_tabela(
            abrir_pagina_gerente.tabela_clientes, dados_esperados_harry
        ), "O resultado da pesquisa na tabela não corresponde ao esperado para 'Harry'"

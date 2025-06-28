class TestCT004:
    """
    Classe de teste para deletar um cliente da lista.
    """

    def test_deletar_cliente(self, abrir_pagina_gerente):
        """
        Testa a deleção de um cliente da tela dos clientes.
        """
        abrir_pagina_gerente.clicar_botao_clientes()
        assert abrir_pagina_gerente.verificar_cabecalho_tabela_clientes(), 'A quantidade de elementos no cabeçalho da tabela é diferente do esperado'
        assert abrir_pagina_gerente.verificar_linhas_tabela_clientes(), 'A quantidade de elementos das linhas da tabela é diferente do esperado'

        abrir_pagina_gerente.deletar_primeiro_cliente()

        assert abrir_pagina_gerente.verificar_cabecalho_tabela_clientes(), 'A quantidade de elementos no cabeçalho da tabela é diferente do esperado'
        assert abrir_pagina_gerente.primeiro_cliente_deletado(), 'O primeiro cliente não foi deletado corretamente'

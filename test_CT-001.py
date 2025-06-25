class TestCT001:
    """
    Classe de teste para criar um cliente.
    """

    def test_adicionar_cliente(self, abrir_pagina_gerente):
        """
        Testa a criação de um novo cliente.
        """
        abrir_pagina_gerente.clicar_botao_adicionar_cliente()
        abrir_pagina_gerente.preencher_campos_adicionar_cliente("joao", "farias", "51000000")
        abrir_pagina_gerente.clicar_botao_enviar_formulario()

        mensagem_alerta = abrir_pagina_gerente.obter_mensagem_alerta()

        assert mensagem_alerta.startswith("Customer added successfully with customer id :"), "A mensagem deveria começar com 'Customer added successfully with customer id :'"

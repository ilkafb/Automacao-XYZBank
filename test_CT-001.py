class TestCT001:
    """
    Classe de teste para criar um cliente.
    """

    def test_adicionar_cliente(self, abrir_pagina_gerente):
        """
        Testa a criação de um novo cliente.
        """
        nome_cliente = "joao"
        sobrenome_cliente = "farias"
        cep_cliente = "51000000"

        abrir_pagina_gerente.clicar_botao_adicionar_cliente()
        abrir_pagina_gerente.preencher_campos_adicionar_cliente(nome_cliente, sobrenome_cliente, cep_cliente)
        abrir_pagina_gerente.clicar_botao_enviar_formulario()

        mensagem_alerta = abrir_pagina_gerente.obter_mensagem_alerta()

        assert mensagem_alerta.startswith("Customer added successfully with customer id :"), "A mensagem deveria começar com 'Customer added successfully with customer id :'"

        abrir_pagina_gerente.fechar_mensagem_alerta()

        abrir_pagina_gerente.clicar_botao_clientes()

        assert abrir_pagina_gerente.verificar_cliente(nome_cliente, sobrenome_cliente, cep_cliente), "O cliente deveria ser encontrado na tabela de clientes"

class TestCT007:
    """
    Classe de teste para criar um cliente existente.
    """

    def test_adicionar_cliente_existente(self, abrir_pagina_gerente):
        """
        Testa a criação de um novo cliente com dados de outro já cadastrado.
        """
        abrir_pagina_gerente.clicar_botao_adicionar_cliente()
        abrir_pagina_gerente.preencher_campos_adicionar_cliente("Hermoine", "Granger", "E859AB")
        abrir_pagina_gerente.clicar_botao_enviar_formulario()

        mensagem_alerta = abrir_pagina_gerente.obter_mensagem_alerta()

        assert mensagem_alerta == "Please check the details. Customer may be duplicate.", "A mensagem deveria ser 'Please check the details. Customer may be duplicate.'"

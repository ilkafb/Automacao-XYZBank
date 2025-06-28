class TestCT002:
    """
    Classe de teste para criar uma conta para um cliente.
    """

    def test_criar_conta_cliente(self, abrir_pagina_gerente):
        """
        Testa a criação de uma conta para um cliente.
        """
        abrir_pagina_gerente.clicar_botao_abrir_conta_cliente()
        abrir_pagina_gerente.abrir_conta_primeiro_cliente()
        abrir_pagina_gerente.clicar_botao_enviar_formulario()

        mensagem_alerta = abrir_pagina_gerente.obter_mensagem_alerta()
        numero_conta = int(mensagem_alerta.split(":")[-1])

        assert mensagem_alerta.startswith("Account created successfully with account Number :"), "A mensagem deveria começar com 'Account created successfully with account Number :'"

        abrir_pagina_gerente.fechar_mensagem_alerta()

        abrir_pagina_gerente.clicar_botao_clientes()

        assert abrir_pagina_gerente.verificar_conta_primeiro_cliente(numero_conta), "A conta do primeiro cliente deveria ser encontrada na tabela de clientes"

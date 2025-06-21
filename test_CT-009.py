class TestCT009:
    """
    Classe de teste para depositar um valor na conta.
    """

    def test_realizar_deposito(self, abrir_pagina_conta_cliente):
        """
        Testa o depósito de um valor na conta e verifica se as informações
        da conta foram atualizadas corretamente.
        """
        valor_a_ser_depositado = 10

        numero_conta_inicial, valor_conta_inicial, moeda_conta_inicial = abrir_pagina_conta_cliente.obter_informacoes()

        abrir_pagina_conta_cliente.clicar_botao_deposito()
        abrir_pagina_conta_cliente.preencher_campo_valor(valor_a_ser_depositado)
        abrir_pagina_conta_cliente.clicar_botao_enviar_formulario()

        numero_conta_final, valor_conta_final, moeda_conta_final = abrir_pagina_conta_cliente.obter_informacoes()

        assert numero_conta_final == numero_conta_inicial, "O numero da conta atual nao corresponde ao numero da conta inicial"
        assert valor_conta_final == valor_conta_inicial + valor_a_ser_depositado, "O valor atual nao corresponde ao valor esperado"
        assert moeda_conta_final == moeda_conta_inicial, "A moeda da conta atual nao corresponde a moeda inicial"
        assert abrir_pagina_conta_cliente.mensagem_visivel(), "A mensagem nao foi exibida"
        assert abrir_pagina_conta_cliente.checar_mensagem("Deposit Successful"), "A mensagem deveria ser 'Deposit Successful'"

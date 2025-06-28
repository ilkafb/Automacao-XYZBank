class TestCT011:
    """
    Classe de teste para retirar um valor na conta maior do que o saldo.
    """

    def test_realizar_saque_saldo_insuficiente(self, abrir_pagina_conta_cliente):
        """
        Testa o saque de um valor na conta maior que o saldo e verifica se exibe a mensagem de falha na trasação.
        """
        valor_a_ser_sacado = 10000

        numero_conta_inicial, valor_conta_inicial, moeda_conta_inicial = abrir_pagina_conta_cliente.obter_informacoes()

        abrir_pagina_conta_cliente.clicar_botao_saque()
        abrir_pagina_conta_cliente.preencher_campo_valor(valor_a_ser_sacado)
        abrir_pagina_conta_cliente.clicar_botao_enviar_formulario()

        numero_conta_final, valor_conta_final, moeda_conta_final = abrir_pagina_conta_cliente.obter_informacoes()

        assert numero_conta_final == numero_conta_inicial, "O numero da conta atual nao corresponde ao numero da conta inicial"
        assert valor_conta_final == valor_conta_inicial, "O valor atual nao corresponde ao valor esperado"
        assert moeda_conta_final == moeda_conta_inicial, "A moeda da conta atual nao corresponde a moeda inicial"
        assert abrir_pagina_conta_cliente.mensagem_visivel(), "A mensagem nao foi exibida"
        assert abrir_pagina_conta_cliente.checar_mensagem("Transaction Failed. You can not withdraw amount more than the balance."), "A mensagem deveria ser 'Transaction Failed. You can not withdraw amount more than the balance.'"

class TestCT012:
    """
    Classe de teste para alterar a conta.
    """

    def test_alterar_conta(self, abrir_pagina_conta_cliente):
        """
        Testa a troca da conta e verifica se as informações.
        """
        numero_conta_inicial, valor_conta_inicial, moeda_conta_inicial = abrir_pagina_conta_cliente.obter_informacoes()

        abrir_pagina_conta_cliente.clicar_botao_alterar_conta("1002")

        numero_conta_final, valor_conta_final, moeda_conta_final = abrir_pagina_conta_cliente.obter_informacoes()

        assert numero_conta_final != numero_conta_inicial, "O numero da conta atual tem que ser diferente do numero da conta inicial"

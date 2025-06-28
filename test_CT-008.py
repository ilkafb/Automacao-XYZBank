class TestCT008:
    """
    Classe de teste para resetar o histórico de transações.
    """

    def test_resetar_historico_transacoes(self, abrir_pagina_transacoes_cliente):
        """
        Testa o reset do histórico de transações.
        """
        quantidade_transacoes_inicial = abrir_pagina_transacoes_cliente.obter_quantidade_transacoes()
        
        assert quantidade_transacoes_inicial > 0, "A quantidade inicial de transações deve ser maior que zero."

        abrir_pagina_transacoes_cliente.clicar_botao_reset()

        assert abrir_pagina_transacoes_cliente.obter_quantidade_transacoes() == 0, "O histórico de transações não foi resetado corretamente."

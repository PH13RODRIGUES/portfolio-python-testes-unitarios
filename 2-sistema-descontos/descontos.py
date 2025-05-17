class CalculadoraDescontos:

    @staticmethod
    def calcular_desconto(valor_compra, eh_cliente_vip=False):

        """
        Calcula desconto progressivo:
        - 5% para compras acima de R$200
        - 10% para compras acima de R$500
        - 15% para VIPs acima de R$500
        - 20% para VIPs acima de R$1000
        """
        
        if not isinstance(valor_compra, (int, float)) or valor_compra < 0:
            raise ValueError("Valor deve ser numérico positivo")

        if eh_cliente_vip:
            if valor_compra > 1000:
                return valor_compra * 0.80
            elif valor_compra > 500:
                return valor_compra * 0.85
        else:
            if valor_compra > 500:
                return valor_compra * 0.90
            elif valor_compra > 200:
                return valor_compra * 0.95

        return valor_compra  # Sem desconto
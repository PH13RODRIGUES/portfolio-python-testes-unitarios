import pytest
from descontos import CalculadoraDescontos

class TestDescontos:
    # Casos Básicos
    def test_sem_desconto(self):
        assert CalculadoraDescontos.calcular_desconto(100) == 100 #(Sem desconto)

    def test_desconto_5_porcento(self):
        assert CalculadoraDescontos.calcular_desconto(300) == 285  # 300 * 0.95  5% desconto


    # Clientes VIP
    def test_vip_desconto_15_porcento(self):
        assert CalculadoraDescontos.calcular_desconto(600, True) == 510  # 600 * 0.85 15% desconto


    def test_vip_desconto_20_porcento(self):    # Retorna: 1700 * 0.80 = 1360
        assert CalculadoraDescontos.calcular_desconto(1700,eh_cliente_vip=True) == 1360     #1700 * 0.80 20% desconto

    # Casos Extremos
    def test_valor_limite_200(self):
        assert CalculadoraDescontos.calcular_desconto(200) == 200  # Limite exato

    def test_valor_negativo(self):
        with pytest.raises(ValueError):
            CalculadoraDescontos.calcular_desconto(-50)

    #Testes de Tipo
    def test_tipo_invalido_string(self):
        with pytest.raises(ValueError):
            CalculadoraDescontos.calcular_desconto("mil reais")
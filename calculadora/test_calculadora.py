import pytest
from calculadora import CalculadoraCientifica
import math

class TestCalculadora:

    # Testes de Adição 
    def test_somar_inteiros(self):
        assert CalculadoraCientifica.somar(2, 3) == 5

    def test_somar_decimais(self):
        assert CalculadoraCientifica.somar(1.5, 2.5) == 4.0

    def test_somar_negativos(self):
        assert CalculadoraCientifica.somar(-1, -1) == -2

    #  Testes de Subtração 
    def test_subtrair_resultado_negativo(self):
        assert CalculadoraCientifica.subtrair(5, 10) == -5

    #  Testes de Divisão 
    def test_dividir_inteiros(self):
        assert CalculadoraCientifica.dividir(10, 2) == 5.0

    def test_dividir_por_zero(self):
        with pytest.raises(ZeroDivisionError):
            CalculadoraCientifica.dividir(10, 0)

    # Testes com Raiz Quadrada
    def test_raiz_quadrada_de_9(self):
        assert CalculadoraCientifica.raiz_quadrada(9) == 3.0

    def test_raiz_quadrada_negativa(self):
        with pytest.raises(ValueError):
            CalculadoraCientifica.raiz_quadrada(-4)

    # Testes com π (Pi) 
    def test_area_circulo_raio_1(self):
        assert CalculadoraCientifica.area_circulo(1) == pytest.approx(math.pi) 
    def test_area_circulo_raio_decimal(self):
        assert CalculadoraCientifica.area_circulo(2.5) == pytest.approx(math.pi * 6.25)

        # Usei pytest.approx() para comparar resultados com floats, evitando falsos negativos devido a arredondamentos



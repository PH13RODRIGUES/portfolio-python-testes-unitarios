import math

class CalculadoraCientifica:
    @staticmethod
    def somar(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Valores devem ser numéricos!")
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero!")
        return a / b

    @staticmethod
    def raiz_quadrada(x):
        if x < 0:
            raise ValueError("Não existe raiz real de número negativo!")
        return math.sqrt(x)

    @staticmethod
    def area_circulo(raio):
        return math.pi * (raio ** 2)
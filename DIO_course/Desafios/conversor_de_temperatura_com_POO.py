#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class conversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahreneit(self):
        return (9/5*celsius)+32


# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = conversorTemperatura(celsius)

fahrenheit = conversorTemperatura.celsius_para_fahreneit(celsius)
print(fahrenheit)
# 1. Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular e escrever o valor da temperatura
# em graus CELSIUS.
# Fórmula: C = 5/9 * (F - 32)

def converterTemperatura(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


def imprimirValor(valor):
    valorArredondado = round(valor, 2)
    print('Valor em Celsius: {0}°C'.format(valorArredondado))


f = float(input("Entre com a temperatura em farenheit: "))
valorConvertido = converterTemperatura(f)
imprimirValor(valorConvertido)

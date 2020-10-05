# 4. Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam
# iguais.

numero1 = int(input('informe um numero: '))
numero2 = int(input('informe outro numero: '))

if numero1 > numero2:
    print('o primeiro numero é o meior: ', numero1)
elif numero1 < numero2:
    print('o segundo numero é o maior:', numero2)
elif numero1 == numero2:
    print('os numeros {} e {} sao iguais'.format(numero1, numero2))

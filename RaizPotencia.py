"""
Este é um programa que calcula a raiz e o quadrado de um número inteiro e positivo.
"""
import math


num = 0
while num <= 0:
    print('Por favor digite um número inteiro e positivo:')
    num = int(input())

    if num > 0:
        print(f'A raiz quadrada de {num} é {math.sqrt(num):.2f}')
        print(f'\nO quadrado do número {num} é : {math.pow(num, 2)}')
    else:
        print('O número Digitado é inválido')







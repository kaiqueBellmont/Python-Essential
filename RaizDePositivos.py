"""
Este é um programa que calcula a raiz de um numero positivo e
mostra a mensagem de invalidez caso ele seja negativo

"""
import math


num1 = 0

while num1 <= 0:

    print('Digite um numero inteiro positivo :')
    num1 = int(input())

    if num1 > 0:
        print(f'A raiz quadrada de {num1} é: {math.sqrt(num1):.2f} ')
    else:
        print('O Número que você digitou é negativo ou inválido.')
    print('Fim do programa')


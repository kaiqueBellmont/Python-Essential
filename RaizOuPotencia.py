"""
Este é um programa que calcula a raiz de um numero positivo e
eleva ao quadrado caso for negativo

"""
import math

print('Digite um numero inteiro:')
num1 = int(input())
if num1 > 0:
    print(f'A raiz quadrada de {num1} é: {math.sqrt(num1):.2f} ')
elif num1 < 0:
    print(f'O quadrado do número {num1} é: {math.pow(num1, 2):.2f} ')
else:
    print('O número que você digitou é inválido')
print('Fim do programa')









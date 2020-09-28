"""
Este é um programa que verifica se o número é par ou ímpar
"""

print('Digite um número inteiro:')
num1 = int(input())

if num1 %2 == 1:
    print(f'O número {num1} é impar.')
elif num1 %2 == 2:
    print(f'O número {num1} é par.')
else:
    print('O programa Só aceita números inteiros...')
    print('Fechando o programa.....')






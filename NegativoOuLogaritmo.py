"""
Este é um programa em que verfifica-se se o numero é positivo,
e se for, calcula-se o logaritmo deste numero;
"""
import math


print("Por favor insira um número positivo:")
numero = float(input())

if numero < 0:
    print(f'{numero} é um Número INVÁLIDO.')
    print("Programa Encerrado.")
    SystemExit
elif numero == 0:
    print('0 é um número neutro, não é positivo nem negativo. È NEUTRO.')
else:
    logaritmo = math.log10(numero)
    print(f'O logaritmo de {numero} é {logaritmo}')
    







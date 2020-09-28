"""
Este é um programa que lê dois números, mostra qual é o maior e a diferença entre eles.
"""
print('Por favor digite o primeiro número:')
num1 = float(input())

print('Por favor digite o segundo número:')
num2 = float(input())

maior = 0
menor = 0

if num1 > num2:
    maior = num1
    menor = num2

else:
    maior = num2
    menor = num1
print(f'O maior número é o {maior:.2f}, e a diferença entre eles é {maior - menor:.2f}')


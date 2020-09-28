"""
18. Este é um programa que converte metros cúbicos para litros
"""
# Fórmula: L = 1000 * M ( Sendo L o volume em litros e M o volume em metros cúbicos)

print("Bem vindo ao conversor de metros cúbicos para litros.")
print("Por favor digite o valor em metros cúbicos: ")

metros_cubicos = float(input())
litros = 1000 * metros_cubicos

# Aqui usei um cast para mostrar os litros em quantidade inteira
print(f'A quantidade de litros é de {int(litros)} litros')




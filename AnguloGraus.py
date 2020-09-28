"""
Este é um programa que converte graus em radianos
"""
# Formula : R = G * pi / 180
# Para definir constantes em python, basta deixar tudo MAIUSCULO
PI = 3.14


print('Por favor, Digite o ângulo em GRAUS :')

graus = (int(input()))
radianos = graus * PI / 180

print(f'O ângulo em radianos é de : {radianos:.2f}')


"""
Este é um programa que converte Radianos em Graus
"""
# Formula : G = R * 180 / PI
# Para definir constantes em python, basta deixar tudo MAIUSCULO
PI = 3.14


print('Por favor, Digite o ângulo em RADIANOS :')

radianos = (float(input()))
graus = radianos *  180 / PI

print(f'O ângulo em GRAUS é de : {graus:.2f}')



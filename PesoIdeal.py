"""
Este é um programa em que calcula-se o peso ideal de uma pessoa de cada sexo;

"""
print('Seja bem vindo ! vamos calcular seu peso idea?')
print("Por favor Digite sua altura:")

altura = str(input())

print("Por favor Digite seu sexo:")
sexo = str(input())

altura1 = altura.replace(',', '.')
sexo1 = sexo.lower()

pesoIdeal = 0

if sexo1 == 'masculino':
    pesoIdeal = (72.7 * float(altura1)) -58
elif sexo1 == 'feminino' :
    pesoIdeal = (62.1 * float(altura1)) -44.7
else:
    print('As informações foram digitadas incorretamente.')
    print('Fim')

print(f'Seu peso ideal é : {pesoIdeal:.2f} KGs')
print('Fim')

"""
Este é um programa em que se calcula a média ponderada de três provas
"""
print("Por favor digite o nome o aluno: ")
nome = str(input())
print("Por favor digite o número da matricula do aluno: ")
matricula = str(input())

"""
# Um jeito:
dados = nome + " " + matricula
print(f'Dados do aluno : {dados}')
"""
print(f'Dados do aluno :')
print(f'Nome :{nome}')
print(f'Matrícula: {matricula}')

print("Os dados do aluno estão corretos? ( Digite a resposta) ")
validacao = str(input())
validacao.lower()

if validacao == "nao" or validacao == "não":
    print("O programa vai ser encerrado agora")
    exit(0)
elif validacao == "sim":
    print("Os dados do aluno foram validados com sucesso.")
else:
    print("Responda com sim ou não")

print("Por favor ao inserir as notas, utilize ponto no lugar da vírgula, caso números quebrados.")
print(f'Por favor digite a nota da primeira prova do aluno {nome} :')
nota1 = float(input())

print(f'Por favor digite a nota da Segunda prova do aluno {nome} :')
nota2 = float(input())

print(f'Por favor digite a nota da Terceira prova do aluno {nome} :')
nota3 = float(input())

mediaFinal = (nota1 * 1) + (nota2 * 1) + (nota3 * 2) / 3

print(f'A média ponderada das três provas é igual a : {mediaFinal:.2f}')
print('Fim')
exit(0)






















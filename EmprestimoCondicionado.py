"""
Este é um progrma qu lÊ o salário de uma pessoa, e condiciona o emprestimo para no máximo 20% do salario
"""
print("Por favor Digite o valor do seu salário:")
salario = str(input())

print(" Por favor digite O valor do empréstimo solicitado:")
emprestimo = str(input())

#criação de variavel para relocar a virgula e o ponto
NovoSalario = salario.replace(',', '.')
NovoEmprestimo = emprestimo.replace(',', '.')

#já convertendo o maximo do valor do empréstimo para uma nova variavel.
ValorMaximo = float(NovoSalario) * 0.2

if float(NovoEmprestimo) <= float(NovoSalario) * 0.2:
    print('Emprestimo Concedido')
else:
    print("Emprestimo Não Cencedido.")
    print("O valor do emprestimo é no MÁXIMO 20% do seu salário")
    print(f'O valor máximo de emprestimo de acordo com seu salário é de R${ValorMaximo:.2f} reais ')















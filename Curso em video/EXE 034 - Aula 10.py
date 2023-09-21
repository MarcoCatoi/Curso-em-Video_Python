# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# para salários superiores a 1250, calcule um aumento de 10%
# para salarios inferiores ou igual a 1250, o aumento é de 15%

sal = float(input('Digite Seu Salário bruto: '))

s_up = float(sal + (sal * 10/100))
s_low = float(sal + (sal * 15/100))

if sal <= 1250:
    print('Seu novo salário depois do aumento será de {}'.format(s_low))
else:
    print('Seu novo salário depois do aumento será de {}'.format(s_up))

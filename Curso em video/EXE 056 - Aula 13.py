"""
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
cont = 0
nome_old = ''
idade_old = 0
cont_m = 0

for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str((input('Digite o Sexo( M / F) da {}ª pessoa: '.format(c)))).lower()
    cont += idade

    if (sexo == 'm') and (idade == idade_old):
        nome_old += ' e o ' + nome
    if (sexo == 'm') and (idade > idade_old):
        idade_old = idade
        nome_old = nome
    if (sexo == 'f') and (idade < 20):
        cont_m += 1
print('''
        ''')
print('A media das idades digitadas é {}: '.format(cont/4))
print('O(s) nome(s) do(s) homem(s) mais velho(s) é: {}'.format(nome_old.title()))
print('Temos {} mulheres menores que 20 anos!'.format(cont_m))

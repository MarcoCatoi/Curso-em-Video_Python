# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente.

nome_dig = str(input('Digite seu nome completo: ')).strip()
nome = nome_dig.split()
x = len(nome) - 1
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu ultimo nome é: {}'.format(nome[x]))

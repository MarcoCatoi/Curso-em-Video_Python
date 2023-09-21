'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

A) O nome com todas as letras maiusculas
B) O nome com todas as letras minusculas
C) Quantas letras ao tdo (sem considerar espaços)
D) Quantas letras tem o primeiro nome

'''

nome = input('Escreva seu nome completo: ')
print('')
print('Prazer em te conhecer', nome)
print('')
print('A) Seu nome com todas as letras maiusculas: ', nome.upper())
print('B) Seu nome com todas as letras minusculas: ', nome.lower())
print('C) Quantidade de letras que tem seu nome sem contar os espaços: ', len(nome.replace(' ', '')))

v_nome = nome.split()
print('D) Quantidade de letras que tem o seu primeiro nome: ', len(v_nome[0]))

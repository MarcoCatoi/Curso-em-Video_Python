"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um numero inteiro: '))
teste = int

for c in range(num-1, 1, -1):
    if num % c == 0:
        teste = 1
        break

if teste == 1:
    print('O numero {} não é primo!'.format(num))
else:
    print('O numero {} é primo!'.format(num))
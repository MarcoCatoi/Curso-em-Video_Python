""" Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
    Se o valor digitado for ímpar, desconsidere-o."""

som = int(0)

for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        som += num
print('''
        ''')
print('O somatório dos numeros pares digitados é: {}!'.format(som))

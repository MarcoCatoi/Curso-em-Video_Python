""" Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
    intervalo de 1 até 500. """

s = int(0)

for c in range(3, 500, 3):
    if c % 2 == 1:
        s = s + c
        print('{}; '.format(c), end='')

print('''

    ''')
print('O somatório dos números impares, multiplos de 3, no intervalo de 1 - 500 é {}!'.format(s))

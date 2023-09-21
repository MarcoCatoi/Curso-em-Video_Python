""" Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles."""
from time import sleep
from emoji import emojize
for c in range(10, -1, -1):
    sleep(1)
    if c == 0:
        print('{}! '.format(c), end='')
    else:
        print('{}; '.format(c), end='')
print('''
        ''')
print('\033[7;40m Feliz ano novo!!!!', '\033[m')
for c in range(0, 10):
    print('\033[7;40m', emojize(':fireworks:'), end='')

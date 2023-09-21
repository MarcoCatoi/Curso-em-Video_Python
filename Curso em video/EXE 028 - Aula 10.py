# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# o programa deverá escrever na tela se o usuário venceu ou errou

import random

num = random.randint(0,5)
adv = int(input('Digite um numero de 0 a 5 que você acredita que o Computador escolheu: '))
if adv == num:
    print('O numero pensado pelo computador é "{}", Parabens você ganhou!'.format(num))
else:
    print('O numero pensado pelo computador é "{}", Infelizmente você perdeu!'.format(num))
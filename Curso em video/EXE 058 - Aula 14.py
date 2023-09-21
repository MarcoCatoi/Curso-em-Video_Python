"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""

from random import choice

cont = 1
while cont != 0:
    x = 0
    m = ''

    while x <= 10:
        m += ' ' + str(x)
        x += 1
    print('+----------------------------------------------------------------------+')
    print('| Olá sou seu computador, e acabei de pensar em um numero de 0 a 10! =D|')
    print('+----------------------------------------------------------------------+')
    print('')
    print('Será que você consegue advinhar?')
    print('')
    esc_hm = str(input('''Qual numero você acha que eu escolhi?
    R= '''))
    esc_pc = choice(m.split())

    while esc_hm != esc_pc:
        if esc_hm not in (m.split()):
            esc_hm = str(input('Sua opção é invalida tente novamente:'))
        else:
            esc_hm = str(input('Voce errou! Tente novamente: '))
    again = str(input('Parabens você acertou! Deseja jogar novamente? S/N: ').upper().strip()[0])
    print(again)

    while again not in 'SN' or again == ''.strip():
        again = str(input('Sua opção foi invalida! Deseja jogar novamente? S/N: ').upper().strip())

    if again == 'N':
        cont = 0
        print('+------------+')
        print('| Bye Bye =D |')
        print('+------------+')

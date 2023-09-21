#  Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
jp = ['Pedra', 'Papel', 'Tesoura']
jphm = str
pc = choice(jp)

hum = str(input('''Escolha uma opção para jogar Jokenpô contra o computador:
                    [1] Pedra
                    [2] Papel
                    [3] Tesoura
                    Opção: '''))
if hum == '1' or hum == '2' or hum == '3':
    if hum == '1':
        jphm = 'Pedra'
    elif hum == '2':
        jphm = 'Papel'
    elif hum == '3':
        jphm = 'Tesoura'

    print('Você escolheu {} e o computador escolheu {}, portanto deu '.format(jphm, pc), end='')
    if jphm == pc:
        print('EMPATE!')
    elif pc == 'Pedra' and jphm == 'Tesoura':
        print('VITÓRIA DO COMPUTADOR!')
    elif pc == 'Papel' and jphm == 'Pedra':
        print('VITÓRIA DO COMPUTADOR!')
    elif pc == 'Tesoura' and jphm == 'Papel':
        print('VITÓRIA DO COMPUTADOR!')
    elif pc == 'Pedra' and jphm == 'Papel':
        print('VITÓRIA DO HUMANO!')
    elif pc == 'Papel' and jphm == 'Tesoura':
        print('VITÓRIA DO HUMANO!')
    elif pc == 'Tesoura' and jphm == 'Pedra':
        print('VITÓRIA DO HUMANO!')
else:
    print('A opção escolhida é invalida, por favor tente novamente!')

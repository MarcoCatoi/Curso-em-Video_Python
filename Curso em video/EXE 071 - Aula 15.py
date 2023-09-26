# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

qtdC = int(0)
print('='*50)
print('|{:^50}|'.format('BANCO CATOI'))
print('='*50)
saque = int(input('Digite um valor inteiro a ser sacado: '))
sobra = saque
while True:

    while saque >= 50:
        qtdC += 1
        saque -= 50
    if qtdC != 0:
        print(f'O caixa irá entregar {qtdC} cedulas de R$ 50,00!')
        qtdC = 0
    while saque >= 20:
        qtdC += 1
        saque -= 20
    if qtdC != 0:
        print(f'O caixa irá entregar {qtdC} cedulas de R$ 20,00!')
        qtdC = 0
    while saque >= 10:
        qtdC += 1
        saque -= 10
    if qtdC != 0:
        print(f'O caixa irá entregar {qtdC} cedulas de R$ 10,00!')
        qtdC = 0
    while saque >= 1:
        qtdC += 1
        saque -= 1
    if qtdC != 0:
        print(f'O caixa irá entregar {qtdC} cedulas de R$ 1,00!')
        qtdC = 0
    if saque == 0:
        break
print('='*50)

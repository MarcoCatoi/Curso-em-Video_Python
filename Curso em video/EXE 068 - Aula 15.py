#   Faça um programa que jogue par ou ímpar com o computador.
#   O jogo só será interrompido quando o jogador perder,
#   mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randrange
vic = 0
name = str(input('Digite seu nome: '))
while True:
    numJ = int(input(f'{name}, digite um numero de 0 a 10: '))
    chcJ = str(input('Escolha PAR ou IMPAR(P|I): ').upper())
    numC = int(randrange(11))
    soma = numJ + numC
    print(f'O numero escolhido pelo adversário foi {numC}!')
    if soma % 2 == 0:
        if chcJ == 'P':
            print(f'{name} venceu!')
            vic = vic + 1
        else:
            break
    else:
        if chcJ == 'I':
            print(f'{name} venceu!')
            vic = vic + 1
        else:
            break
print(f'{name}, perdeu! O numero de vitórias consecutivas foi de {vic} vez(es)!\n\n')
print('Fim de Jogo!')
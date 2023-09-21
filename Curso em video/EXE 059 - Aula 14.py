"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um outro numero inteiro: '))
opcao = str()

while opcao != '5':
    print('Abaixo há algumas opções!')
    print('+-----------------------+')
    print('|[ 1 ] Somar            |')
    print('|[ 2 ] Multiplicar      |')
    print('|[ 3 ] Qual o Maior     |')
    print('|[ 4 ] Novos Numeros    |')
    print('|[ 5 ] Sair do programa |')
    print('+-----------------------+')
    opcao = str(input('Qual a opção que deseja? '))
    print('')
    if opcao == '1':
        soma = int(num1 + num2)
        print('O resultado da soma é: {}'.format(soma))
        print('')
    elif opcao == '2':
        mtp = int(num1 * num2)
        print('O resultado da multiplicação é: {}'.format(mtp))
        print('')
    elif opcao == '3':
        maior = ''
        if num1 > num2:
            maior = int(num1)
        elif num1 < num2:
            maior = int(num2)
        else:
            print('Os numeros são iguais!')
            print('')
        if maior != '':
            print('O maior entre os numeros é: {}'.format(maior))
            print('')
    elif opcao == '4':
        num1 = int(input('Digite um novo numero inteiro: '))
        num2 = int(input('Digite um outro novo numero inteiro: '))
    elif opcao == '5':
        print('+----------------------------------------+')
        print('| Foi excelente fazer negócios com você! |')
        print('+----------------------------------------+')
    else:
        print('Opção inválida tente novamente! ')
        print('')

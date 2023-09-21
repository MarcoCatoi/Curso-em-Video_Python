# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))

op = int(input('''Escolha uma das opções para conversão:
                [1] Binário
                [2] Hexadecimal
                [3] Octal
                Opção: '''))
if op == 1:
    print('O numero convertido para binário é {}'.format(bin(num)[2:]))
elif op == 2:
    print('O numero convertido para hexadecimal é {}'.format(hex(num)[2:]))
elif op == 3:
    print('O numero convertido para octal é {}'.format(oct(num)[:2]))
else:
    print('Sua opção é inválida!')

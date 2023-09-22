#  Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

dec = 'S'
lista = str('')
soma = int(0)
cont = int(0)
mayor = int(0)
minor = int(0)
media = float
while dec != 'N':
    num = int(input('Digite um numero inteiro: '))
    cont += 1
    soma += num

    if lista == '':
        lista = '{}'.format(str(num))
    else:
        lista = '{}, {}'.format(lista, str(num))

    if num > mayor:
        mayor = num
    if num < minor:
        minor = num
    if minor == 0:
        minor = num

    dec = str(input('Você deseja continuar digitando?(S/N) :')).upper()
media = soma/cont
print('\n'
      'Os numeros digitados está na lista abaixo:\n'
      '|{}|\n'.format(lista))
print('A média dos numeros digitados é {:.2f}.\n'.format(media))
print('O maior numero digitado é {} e o menor é {}.'.format(mayor, minor))

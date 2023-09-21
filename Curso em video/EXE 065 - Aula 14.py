#  Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int
maior = int(0)
menor = int
cont = int(0)
soma = int(0)
media = float
dec = str

while dec != 'N':
    num = input('Digite um numero: ')
    num = int
    soma = soma + int(num)
    cont = cont + 1
    media = soma/cont
    if num > maior:
        maior = int(num)
    elif num < menor:
        menor = int(num)
    else:
        menor = maior
    dec = input('Deseja continuar digitando? S/N:  ').upper
print('O maior entre os numeros digitados foi {} e o menor foi {}.'
      'A média entre os numeros digitados foi de {}.format(maior, menor, media)')


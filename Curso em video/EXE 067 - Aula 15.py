#   Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#   O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    for x in range(0, 10, 1):
        res = x * num
        print(f'|{x} X {num} = {res}|')





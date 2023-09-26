# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = int(0)
cont = int(0)
soma = int(0)

while cont != '999':
    cont = input('Digite um numero para ser somado.(Quando quiser encerrar digite o numero "999":')
    soma = soma + int(cont)
    n = n + 1
soma = soma - 999
n = n - 1
print('A quantidade de numeros digitados é: {} '
      'e o resultado da soma dos numeros digitados é: {}'.format(n, soma))

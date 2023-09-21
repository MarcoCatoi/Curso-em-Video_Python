'''
Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

unidade, dezena, centena, milhar
'''
num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A Unidade é: ', u)
print('A dezena é: ', d)
print('A centena é: ', c)
print('O milhar é: ', m)


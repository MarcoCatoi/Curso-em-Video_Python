# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
print('======================')
print('SEQUENCIA DE FIBONACCI')
print('======================')
n = int(input('Digite a quantidade de termos que voce deseja mostrar da sequencia de fibonacci: '))
cont = 0
t1 = int(0)
t2 = int(1)
pn = int
sf = str('{}, {}'.format(t1, t2))

while cont != n:
    cont = cont + 1
    pn = t1 + t2
    t1 = t2
    t2 = pn
    sf = sf + ', {}'.format(str(pn))
print('|{}|'.format(sf))

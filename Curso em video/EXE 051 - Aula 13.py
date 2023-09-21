""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
    No final, mostre os 10 primeiros termos dessa progressão."""

n = int(input('Digite um numero inteiro para ser o primeiro termo de uma PA: '))
r = int(input('Digite um numero inteiro para ser a razão da mesma PA: '))
nn = int(0)
pa = ''

for c in range(2, 11):
    nn = n + ((c-1) * r)
    if c != 1:
        pa += str(nn) + '; '
    else:
        pa += str(nn)
print('Os 10 primeiros termos da P.A presente é: {} '.format(pa))

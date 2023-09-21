"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
n = int(input('Digite o primeiro termo de uma P.A.: '))
r = int(input('Digite a razão dessa mesma P.A.: '))
c = 1
pa = ''
while c <= 10:
    nn = n + ((c-1) * r)
    if c != 10:
        pa += str(nn) + '; '
    else:
        pa += str(nn)
    c += 1
print('Os 10 primeiros termos da P.A. é | {} | '.format(pa))

'''
Condição

if condição:
else:
'''

n1 = float(input('Digite sua Primeira Nota: '))
n2 = float(input('Digite sua Segunda Nota: '))
m = (n1+n2)/2

print('A sua media foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('sua média não foi boa, estude mais!')
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite um ano usando os 4 digitos: '))

abp = str('O ano digitado é bissexto!')
abn = str('O ano digitado não é bissexto!')

t1 = int(ano % 100)
t2 = int(ano % 400)

if t1 == 0 and t2 == 0:
    print(abp)
    print('cond a')
else:
    if t1 != 0 and ano % 4 == 0:
        print(abp)
        print('cond b')
    else:
        print(abn)
        print('cond c')

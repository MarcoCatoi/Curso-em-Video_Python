"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""
fat = 1
cont = str()
trc = ''

num = int(input('Digite um numero para que seja feito seu fatorial: '))
num_v = num

while num != 0:
    fat *= num
    if num != 1:
        cont += str(num) + ' * '
    else:
        cont += str(num)
    trc += ((len(str(num))) * '-') + '---'
    num -= 1

trc += ('-' * len(str(fat))) + '-+'
print('''O fatorial do numero {} é
+-{}
| {} = {} |
+-{}
'''.format(num_v, trc, cont, fat, trc))

"""
    Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

num = int(input('Digite um numero inteiro: '))
tab = int(0)

print('============== TABUADA DE {} =============='.format(num))
for c in range(0, 11):
    tab = num * c
    print('|| {} * {} = {} ||'.format(num, c, tab))
print('===========================================')
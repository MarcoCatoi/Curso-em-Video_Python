"""
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

"""frase = str(input('Digite uma frase: ').strip().lower().replace(' ', ''))
frase_inv = frase[::-1]
print(frase)
print(frase_inv)

if frase == frase_inv:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')"""

frase = (input('Digite uma frase: ').strip().lower().replace(' ', ''))
frase_inv = ''

for c in range(len(frase)-1, -1, -1):
    frase_inv += frase[c]

if frase == frase_inv:
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada não é um palindromo!')


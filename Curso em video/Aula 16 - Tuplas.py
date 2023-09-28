# Tuplas é uma forma de ter um variável composta, porém imutável

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  # A tupla geralmente é definida com parenteses mas não é necessário

len(lanche)  # conta quantos elementos tem dentro da tupla (resposta 4)

print(lanche[1:])  # irá imprimir na tela de suco a pudim, mesmo conceito de fatiamento de string

for comida in lanche:
    print(f' Eu comi {comida}')  # Nesse caso o for ele vai contabilizar todos elemento e fazer 'comida' receber cada um

del lanche  # Unica alteração que podemos fazer em uma tupla é deleta-la

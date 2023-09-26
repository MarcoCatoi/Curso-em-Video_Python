# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

total = float(0.00)
moreT = int(0)
cheap = str('')
priceMC = float(0.00)
while True:
    nameP = str(input('Digite o nome do produto comprado: '))
    price = float(input('Digite o preço do produto comprado: R$'))
    total += price
    if price > 1000.00:
        moreT += 1
    if priceMC == 0.00:
        priceMC = price
        cheap = nameP
    elif price < priceMC:
        priceMC = price
        cheap = nameP
    chc = str(input('Deseja continuar sua compra? S|N ---> ').upper())
    if chc == 'N':
        break
print(f'O total gasto na compra foi de R${total:.2f}!\n'
      f'{moreT} produtos foram mais que R$1000.00!\n'
      f'O Produto mais barato da sua compra foi o(a) {cheap}!')

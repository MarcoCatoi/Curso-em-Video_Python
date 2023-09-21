# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros

p_real = float(input('Digite qual o valor do produto: '))
mtd_pag = int(input('''Qual a forma de pagamento? Digite :
                    [1] A vista no Dinheiro ou cheque.
                    [2] A visa no cartão.
                    [3] 2x no cartão.
                    [4] 3x ou mais no cartão.
                    Opção: '''))

if mtd_pag == 1:
    print('Você ganhou 10% de desconto, portanto irá pagar R$ {:.2f}!'.format(p_real - (p_real * 0.1)))
elif mtd_pag == 2:
    print('Você ganhou 5% de desconto, portanto irá pagar R$ {:.2f}!'.format(p_real - (p_real * 0.05)))
elif mtd_pag == 3:
    print('Você não ganhou desconto, portanto irá pagar R$ {:.2f}!'.format(p_real))
elif mtd_pag == 4:
    print('Você gterá que pagar 20% de juros, portanto irá pagar R$ {:.2f}!'.format(p_real + (p_real * 0.2)))
else:
    print('Método de pagamento invalido! Tente novamente')

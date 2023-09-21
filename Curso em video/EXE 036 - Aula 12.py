# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

v_casa = float(input('Escreva o valor da casa: '))
sal = float(input('Digite seu salário bruto: '))
ano = int(input('Em quantos anos você pretende parcelar o imóvel? '))

mes = ano * 12
c_base = v_casa / mes
pct = sal * (30/100)
teste = bool(c_base <= pct)

print('Parcela mensal: R$ {:.2f}'.format(c_base))
print('30% do salário equivale a R$ {:.2f}'.format(pct))

if teste:
    print('Parabens você pode financiar este imóvel!')
else:
    print('Infelizmente você não pode financiar o imóvel, pois o valor'
          'da parcela mensal é maior do que 30% do seu salário.')

# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem,
# cobrando R$ 0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas

dis = float(input('Digite a distancia em km que da a viagem em questão:'))
if dis <= 200:
    val = float(dis * 0.50)
else:
    val = float(dis * 0.45)
print('O valor da sua viagem ficou em {:2} Reais'.format(val))


# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80KM/h,
# mostre uma msg dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada KM/h acima do permitido

vel = int(input('Qual a velocidade atual em km do seu carro: '))
x = float(vel - 80)
val = float(x * 7.00)
if vel > 80:
    print('A velocidade permitida é de 80Km/h, você foi multado por estar {:.3} km/h da velocidade permitida!'
          ' Diminua a velocidade!'.format(x))
    print('Pelo calculo sua multa foi no valor de R${:.5}'.format(val))
else:
    print('Parabens você está dentro velocidade permitida =D  !')

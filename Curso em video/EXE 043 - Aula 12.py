# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

a = int(input('Digite sua altura em centimetros: '))
pkg = float(input('Digite seu peso em kilograma: '))

amt = a / 100
imc = pkg / (amt ** 2)

print(pkg)
print(amt)

if imc < 18.5:
    print('Seu IMC é {:.2f}. Você esta abaixo do peso!'.format(imc))
elif (imc >= 18.5) and (imc < 25):
    print('Seu IMC é {:.2f}. Você esta no peso ideal!'.format(imc))
elif (imc >= 25) and (imc < 30):
    print('Seu IMC é {:.2f}. Você esta com sobrepeso!'.format(imc))
elif (imc >= 30) and (imc <= 40):
    print('Seu IMC é {:.2f}. Você esta na Obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}. Você esta na obesidade mórbida!'.format(imc))


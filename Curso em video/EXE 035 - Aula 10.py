# Desenvolva um programa que leia o comprimento de trÊs retas e diga ao usuário se podem ou não formar um triângulo

r1 = float(input('Digite um tamanho para determinar uma reta:'))
r2 = float(input('Digite um tamanho para determinar uma outra reta:'))
r3 = float(input('Digite um tamanho para determinar mais uma reta:'))

if abs((r2-r3)) < r1 < (r2+r3):
    if abs((r1-r3)) < r2 < (r1+r3):
        if abs((r2 - r1)) < r3 < (r2 + r1):
            print('É possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo!')

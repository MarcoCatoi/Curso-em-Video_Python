# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = float(input('Digite um tamanho para determinar uma reta: '))
r2 = float(input('Digite um tamanho para determinar uma outra reta: '))
r3 = float(input('Digite um tamanho para determinar mais uma reta: '))

if abs((r2-r3)) < r1 < (r2+r3):
    if abs((r1-r3)) < r2 < (r1+r3):
        if abs((r2 - r1)) < r3 < (r2 + r1):
            if r1 == r2 == r3:
                print('É possivel formar um triangulo, e esse triângulo é EQUILATERO!')
            elif ((r1 == r2) or (r1 == r3) or (r2 == r3)) and ((r1 != r2) or (r1 != r3) or (r2 != r3)):
                print('É possivel formar um triangulo, e esse triângulo é ISÓSCELES!')
            elif r1 != r2 != r3:
                print('É possivel formar um triangulo, e esse triângulo é ESCALENO!')
else:
    print('Não é possivel formar um triangulo!')


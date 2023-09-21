"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""
comp = 0
while comp == 0:
    sexo = str(input("Digite seu sexo (M/F): ").upper().strip())
    if sexo == 'F' or sexo == 'M':
        comp = '1'
        if sexo == 'F':
            print("Olha que legal seu sexo é Feminino!")
        elif sexo == 'M':
            print("Olha que legal seu sexo é Masculino")
    else:
        print("Você digitou a opção invalida, tente novamente!")

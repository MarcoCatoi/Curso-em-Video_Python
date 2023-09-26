#   Crie um programa que leia a idade e o sexo de várias pessoas.
#   A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
men = int(0)
wom = int(0)
major = int(0)
while True:
    idade = int(input('Digite sua Idade: '))
    sexo = str(input('Digite seu sexo (F|M): ').upper())
    if idade > 18:
        major += 1
    if sexo == 'M':
        men += 1
    elif sexo == 'F' and idade < 20:
        wom += 1
    chc = str(input('Deseja continuar digitando (S|N)? ').upper())
    if chc == 'N':
        break
print(f'Foram cadastrados {major} maiores de 18 anos!'
      f'Foram cadastrados {men} do sexo masculino!'
      f'Foram cadastrados {wom} do sexo feminino menor de 20 anos!')

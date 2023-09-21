""" Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date

ano_atual = int(date.today().year)
idade = int
contd = int(0)
contu = int(0)

for c in range(0, 7):
    ano = int(input('Digite o seu ano de nascimento: '))
    if (ano_atual - ano) < 21:
        contd += 1
    else:
        contu += 1
print('Das 7 pessoas entrevistadas, {} não atingiram a maioridade e {} Já são maiores.'.format(contd, contu))

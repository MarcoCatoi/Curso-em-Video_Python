# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano_nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    print('Acalma teu coração, ainda falta {} para você se alistar'.format(18 - idade))
elif idade == 18:
    print('Olha que legal, ja está na hora de você se alistar!')
else:
    if (idade - 18) == 1:
        print('Vish, ja passou {} ano do tempo para voce se alistar!'.format(idade - 18))
    else:
        print('Vish, ja passou {} anos do tempo para voce se alistar!'.format(idade - 18))

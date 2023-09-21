# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

ano_nasc = int(input('Caro atleta digite seu ano de nascimento: '))
mes_nasc = int(input('Caro atleta digite seu mês de nascimento: '))
dia_nasc = int(input('Caro atleta digite seu dia de nascimento: '))

ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day
idade = int

if mes_nasc < mes_atual:
    idade = ano_atual - ano_nasc
elif mes_nasc == mes_atual:
    if dia_nasc > dia_atual:
        idade = (ano_atual - ano_nasc) - 1
    else:
        idade = ano_atual - ano_nasc
elif mes_nasc > mes_atual:
    idade = (ano_atual - ano_nasc) - 1

if idade <= 9:
    if idade == 0:
        print('Sua idade é {} ano, você é muito novinho! Mas sua categoria é Mirim.'.format(idade))
    elif idade == 1:
        print('Sua idade é de {} ano, portanto, sua categoria é Mirim!'.format(idade))
    else:
        print('Sua idade é de {} anos, portanto, sua categoria é Mirim!'.format(idade))
elif 9 < idade <= 14:
    print('Sua idade é de {} anos, portanto, sua categoria é infantil!'.format(idade))
elif 14 < idade <= 19:
    print('Sua idade é de {} anos, portanto, sua categoria é Junior!'.format(idade))
elif 19 < idade <= 25:
    print('Sua idade é de {} anos, portanto, sua categoria é Senior!'.format(idade))
else:
    print('Sua idade é de {} anos, portanto, sua categoria é Master!'.format(idade))

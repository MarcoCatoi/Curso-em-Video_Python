# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

ext = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',\
      'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    num = int(input('Digite um número de 0 a 20 para ser escrito por extenso: '))
    if 0 <= num <= 20:
        print(f'O numero que você escolheu foi o {ext[num].capitalize()}!')
        dec = str(input('Deseja continuar digitando: ')[0].strip().upper())
        if dec == 'N':
            break
    else:
        print('Você digitou um número invalido, digite novamente!', end=' ')

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"

'''cidade_dig = input('Em que cidade você nasceu?: ')
cidade = cidade_dig.split()
print('Santo' in cidade[0])
'''

cidade = str(input('Em que cidade você nasceu?: ')).strip()
print(cidade[:5].upper() == 'SANTO')

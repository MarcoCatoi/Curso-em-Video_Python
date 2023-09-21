# if cond :
# elif cond :
# else:

nome = str(input('Digite seu nome:'))

if nome == 'Catoi':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == "Ana":
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

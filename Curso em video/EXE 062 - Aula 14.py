"""
Melhore o exercicio 61 perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
resp = 10

n = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
c = 1
pa = ''
ini = 0
while resp != 0:
    while c <= resp:
        nn = n + ((c-1) * r)
        if c != resp:
            pa += str(nn) + '; '
        else:
            pa += str(nn)
        c += 1
    c = 1
    n = n + (resp * r)
    if ini == 0:
        print('Os {} primeiros termos da P.A. é: |{}|'.format(resp, pa))
    else:
        print('Os {} Próximos termos da P.A. são: |{}|'.format(resp, pa))
    print('')
    ini = 1
    resp = int(input('Você deseja ver mais termos? Se sim digite quantos, se não digite 0: '))
    pa = ''
print('')
print('Tchau!')

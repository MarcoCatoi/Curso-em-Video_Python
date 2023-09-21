# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Parabens pequeno gafanhoto, você foi aprovado com uma média de \033[32m{}\033[m.'.format(media))
elif (media >= 5) and (media < 7):
    print('Que pena amiguinho, você não conseguiu a nota, mas ainda há uma chance! sua media foi de \033[34m{}\033[m.'
          .format(media))
else:
    print('Não foi dessa vez queridão, espero que o proximo ano você estude mais! sua média foi de \033[31m{}\033[m.'
          .format(media))

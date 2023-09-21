'''
Faça um programa que leia uma frase pelo teclado e mostre:

*quantas vezes aparece a letra "A"
*Em que posição ela aparece a primeira vez
*Em que posição ela aparece a ultima vez

'''

frase = str(input('Digite uma frase: ').strip())
print('A sua frase tem {} letra(as) "A".'.format(frase.upper().count('A')))
print('A posição que ela aparece a primeira vez é {}'.format((frase.upper().find('A')+1)))
print('A posição que ela aparece a ultima vez é {}'.format((frase.upper().rfind('A',)+1)))

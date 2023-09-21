""" Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

p_up = float(0)
p_down = float(1000)

for c in range(0, 5):
    peso = float(input('Digite seu Peso: '))
    if peso > p_up:
        p_up = peso
    if peso < p_down:
        p_down = peso

print('O maior peso digitado foi {}KG, e o menor foi {}KG.'.format(p_up, p_down))
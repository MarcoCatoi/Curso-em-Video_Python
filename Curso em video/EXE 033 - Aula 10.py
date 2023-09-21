# Faça um programa que leia 3 numeros e mostre qual é o maior e o menor

num1 = int(input('Digite um numero Inteiro: '))
num2 = int(input('Digite um outro numero Inteiro: '))
num3 = int(input('Digite mais um  numero Inteiro: '))

if num1 > num2 > num3:
    print('o maior numero é o numero {}'.format(num1))
    print('o menor numero é o numero {}'.format(num3))
else:
    if num1 > num3 > num2:
        print('o maior numero é o numero {}'.format(num1))
        print('o menor numero é o numero {}'.format(num2))
    else:
        if num2 > num1 > num3:
            print('o maior numero é o numero {}'.format(num2))
            print('o menor numero é o numero {}'.format(num3))
        else:
            if num2 > num3 > num1:
                print('o maior numero é o numero {}'.format(num2))
                print('o menor numero é o numero {}'.format(num1))
            else:
                if num3 > num1 > num2:
                    print('o maior numero é o numero {}'.format(num3))
                    print('o menor numero é o numero {}'.format(num2))
                else:
                    if num3 > num2 > num1:
                        print('o maior numero é o numero {}'.format(num3))
                        print('o menor numero é o numero {}'.format(num1))

frase = 'Curso em Video Python'
print(frase)

# Fatiamento

'''
frase[X1:X2:x3]
X1 -> Inicio
X2 -> Fim (-1)
X3 -> Vai pulando de caracter em caracter

frase[:X1]
Dois pontos antes faz começar do inicio ate o X1

frase[X1:]
Dois pontos antes faz começar do X1 ate o Final
'''
print('Fatiamento')
print('frase[9] = "V"')
print(frase[9])

print('frase[3:8] = "so em"')
print(frase[3:8])

print('frase[4:17:2] = "oe ie y"')
print(frase[4:17:2])

print('frase[:3] = "Cur"')
print(frase[:3])

print('frase[17:] = "thon"')
print(frase[17:])

# Análise

# Len(frase) -> Comprimento da string
print('len(frase) = "21"')
print(len(frase))

# cont('X') -> Vai contar qnts vezes existe o 'X' na string
print('frase.count("o") = "3"')
print(frase.count('o'))

# cont('x',i,n) -> vai contar qnts vezes existe o 'X' na string de i até n-1
print('frase.count("o, 9, 21") = "2"')
print(frase.count('o', 0, 21))

# find('XYZ') -> Vai me dizer onde tem na string 'XYZ' se caso não existe ele retorna o valor -1,
#                ou seja, não foi encontrado
print('frase.find("Jeringonça") = "-1"')
print(frase.find('Jeringonça'))

# Transformação

# replace('X', 'Y') -> Vai substituir na string o 'X' pelo 'Y'
print('frase.replace("Python","Android") = "Curso em Video Android"')
print(frase.replace('Python', 'Android'))

# upper() -> Vai deixar todos caracteres da string maiusculos
print('frase.upper() = "CURSO EM VIDEO PYTHON"')
print(frase.upper())

# lower() -> Vai deixar todos caracteres da string minusculos
print('frase.lower() = "curso em video python"')
print(frase.lower())

# capitalize() -> vai colocar toda string em minusculo e apenas o primeiro caracter em maiusculo
print('frase.capitalize() = "Curso em video python"')
print(frase.capitalize())

# title() -> Vai usar o espaço como quebra de palavras e colocar a primeira letra de cada
#            palavra em maiusculo
print('frase.title() = "Curso Em Video Python"')
print(frase.title())

# strip() -> remove espaços inuteis (fim e inicio)
# rstrip() -> remove espaços inuteis no lado direito da string
# lstrip() -> remove espaços inuteis no lado esquerdo da string

# Divisão e Junção

# split() -> gera uma lista com todas as palavras em uma string
# 'x'.join(frase) -> faz a separação dos caracteres da string com 'x'
print('"-".join(frase) = "Curso Em Video Python"')
print('-'.join(frase.split()))

'''
Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, 
quantos números sortudos existem entre 18644 e 33087, incluindo os extremos.
'''
numeros = 0

for x in range(18644, 33088):
    if '2' in str(x) and '7' not in str(x):
        numeros = numeros + 1 

print(numeros)

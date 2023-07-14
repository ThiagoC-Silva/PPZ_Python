'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte aquantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos
dias de vida um fumante perderá. Exiba o total de dias
'''
quanti_cigarros = int(input('Quantidade de cigarros diários: '))
anos = int(input('Anos como fumante: '))
minutos = quanti_cigarros * anos * 365 * 10
dias = (minutos/60)/24

print(f'Dias perdidos: {dias:.0f}')


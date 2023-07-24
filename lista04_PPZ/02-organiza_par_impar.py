'''
Sorteie 20 inteiros entre 1 e 100 num a lista. Armazene os números pares
na lista PAR e os números ímpares na lista IMPAR. Imprima a s três listas
'''
import random

lista_geral = random.sample(range(101), 20)
lista_par = []
lista_impar = []

for cont in lista_geral:
    
    if cont%2==0: lista_par.append(cont)
    else: lista_impar.append(cont)

print(f'Lista geral: {lista_geral}')
print(f'Lista de pares: {lista_par}')
print(f'Lista de ímpares: {lista_impar}')
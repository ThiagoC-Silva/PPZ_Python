'''
Sorteie 10 inteiros entre 1 e 100 para uma lista
e descubra o maior e o menor valor, sem usar as 
funções max e min.
'''
import random

numeros = []
numeros = random.sample(range(1,101), 10)
maior = menor = numeros[0]
indice = 0

for cont in numeros:

    if cont > maior: maior = cont
    if cont < menor: menor = cont
    indice = indice + 1

print(f'Conjunto: {numeros}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
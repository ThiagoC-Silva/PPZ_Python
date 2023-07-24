'''
Faça um programa que crie dois vetores com 10 elementos aleatórios 
entre 1 e 100. Gere um terceirovetor de 20 elementos, cujos valores 
deverão ser compostos pelos elementos intercalados dos dois outros vetores.
Imprima os três vetores
'''
from random import sample
vetor1 = sample(range(101), 10)
vetor2 = sample(range(101), 10)
vetor3 = []

for cont in range(10):
    vetor3.append(vetor1[cont])
    vetor3.append(vetor2[cont])

print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'Vetor 3: {vetor3}')
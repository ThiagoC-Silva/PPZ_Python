'''
Faça um Programa que leia três números e mostre o maior deles.
'''
n1 = int(input('Informe um número: '))
n2 = int(input('Informe um número: '))
n3 = int(input('Informe um número: '))
maior = 0

if n1>n2 and n1>n3:
    maior = n1
elif n2>=n3:
    maior = n2
else:
    maior = n3

print(f'Maior número informado: {maior}')
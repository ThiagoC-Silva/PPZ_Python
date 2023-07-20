'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
n1 = int(input('Informe um número: '))
n2 = int(input('Informe um número: '))
n3 = int(input('Informe um número: '))

if n1>n2 and n1>n3:
    maior = n1
elif n2>=n3:
    maior = n2
else:
    maior = n3

if n1<n2 and n1<n3:
    menor = n1
elif n2<=n3:
    menor = n2
else:
    menor = n3

print(f'Maior número informado: {maior}')
print(f'Menor número informado: {menor}')
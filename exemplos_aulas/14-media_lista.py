'''
leia 4 notas e informe a media 
'''
notas = []
cont = 0
soma = 0

while cont < 4:
    notas.append(float(input(f'{cont+1}° nota: ')))
    soma = soma + notas[cont]
    media = soma/len(notas)
    cont = cont + 1

print(f'Média {notas}: {media:.1f}')
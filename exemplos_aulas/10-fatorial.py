fatorial = 1
cont = 2
fim = int(input('Fatorial de: '))

while cont <= fim:
    fatorial = fatorial * cont
    cont = cont + 1

print(f'Fatorial de {fim} é {fatorial}')
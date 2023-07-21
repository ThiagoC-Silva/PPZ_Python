cont = 1
soma = 0

while cont <= 10:
    num = int(input(f'Digite o {cont}° valor: '))
    soma = soma + num 
    cont = cont + 1

print(f'Soma total = {soma}')
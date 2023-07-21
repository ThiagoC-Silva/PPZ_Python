cont = 1
soma = 0
while cont <= 10:
    num = int(input(f'Digite o {cont}° valor: '))
    cont = cont + 1
    soma = soma + num

print(f'Média total = {soma/10:.1f}')
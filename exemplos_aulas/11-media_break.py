soma = 0
cont = 0

while True:
    valor = int(input('Valor: '))
    if valor == 0:
        break
    else:
        cont = cont + 1
        soma = soma + valor
    
print(f'Media total: {soma/cont:.1f}')
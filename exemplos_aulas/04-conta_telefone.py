minutos = int(input('Minutos: '))
 
if minutos < 200:
    taxa = 0.2
else:
    if minutos <= 400:
        taxa = 0.18
    if minutos > 400 and minutos <= 800:
        taxa = 0.15
    else:
        taxa = 0.8

print(f'Conta: R${minutos * taxa}')
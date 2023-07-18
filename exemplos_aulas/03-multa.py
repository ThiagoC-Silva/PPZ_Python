velocidade = int(input('Informe a velocidade do carro (km): '))

if velocidade > 110:
    print('Motorista multado.')
    multa = (velocidade - 110) * 5
    print(f'Valor da multa: R${multa}')
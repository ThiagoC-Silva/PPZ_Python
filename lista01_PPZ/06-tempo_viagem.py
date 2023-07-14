'''
Calcule o tempo de uma viagem de carro. Pergunte a distância 
a  percorrer e a velocidade média esperada para a viagem.
'''
distancia = float(input('Distancia a percorrer: '))
veloMedia = float(input('Velocidade média: '))

print(f'Tempo: {distancia/veloMedia:.2f}')

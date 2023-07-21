'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
o algoritmo de Euclides
'''
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

while num1%num2!=0:
    num1, num2 = num2, (num1%num2)

print(num2)
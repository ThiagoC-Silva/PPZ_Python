'''
Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''
l1 = int(input('lado 1 do triâgulo: '))
l2 = int(input('lado 2 do triâgulo: '))
l3 = int(input('lado 3 do triâgulo: '))

if l1>l2+l3 or l2>l1+l3 or l3>l2+l1:
    print('Não é um triâgulo.')
elif l1==l2==l3:
    print('Triângulo: Equilátero')
elif l1==l2 or l1==l3 or l2==l3:
    print('Triângulo: Isósceles')
else:
    print('Triângulo: Escaleno')
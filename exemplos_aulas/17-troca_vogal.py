'''
Faça um programa que leia uma palavra e troqe as vogais
por "*"
'''
#obs: operador 'in' = dentro 
palavra:str = input('Palavra: ')
cont = 0
sem_vogal = ''

while cont < len(palavra):
    if palavra[cont] in 'aeiou':
        sem_vogal = sem_vogal + '*'
    else:
        sem_vogal = sem_vogal + palavra[cont]
    cont = cont + 1

print(sem_vogal)
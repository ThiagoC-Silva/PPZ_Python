'''
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e aporcentagem 
do aumento. Exiba o valor do aumento e do novo salário
'''
salario = float(input('Salário atual: '))
porcentagem = int(input('Porcentagem de aumento: '))
aumento = salario * (porcentagem/100)
print(f'Aumento: R${aumento}')
print(f'Reajuste salarial: R${salario+aumento:.2f}')
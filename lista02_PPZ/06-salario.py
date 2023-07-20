'''
Faça um Programa que pergunte quanto vocêganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe queSalário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a.+ Salário Bruto : R$
b.-IR (11%) : R$
c.-INSS (8%) : R$
d.-Sindicato ( 5%) : R$
e.= Salário Liquido : R$
'''
hora = float(input('Ganha por hora: R$'))
horas_trabalhadas = int(input('Horas trabalhadas: '))
salario_bruto = hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto*0.05
desconto = ir + inss + sindicato

salario_liquido = salario_bruto - desconto

print(f'Salário Bruto: R$ {salario_bruto}')
print(f'IR: R$ {ir}')
print(f'INSS: R$ {inss}')
print(f'Sindicato: R$ {sindicato}')
print(f'Salário Líquido: R$ {salario_liquido}')


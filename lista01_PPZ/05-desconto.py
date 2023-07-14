'''
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e opreço a pagar
'''
valor = float(input('Preço: '))
desconto = int(input('Porcentagem de desconto: '))
desconto *= valor/100  

print(f'Desconto: R${desconto}')
print(f'Pagar: R${valor-desconto:.2f}')

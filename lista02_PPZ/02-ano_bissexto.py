'''
Determine se um ano é bissexto.
'''
ano = int(input('ANO: '))

if ano%4==0 and ano%100!=0:
    print('Ano bissexto!')
elif ano%100==0 and ano%400==0:
    print('Ano bissexto!')
else:
    print('Ano não bissexto.')

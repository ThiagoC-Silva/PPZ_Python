mes = '''janeiro fevereiro março abril
maio junho julho agosto
semtembro outubro novembro dezembro'''.split()

dd,mm,aaaa = input('dd/mm/aaaa: ').split('/')
mm = int(mm)

print(f'{dd} de {mes[mm-1]} de {aaaa}')
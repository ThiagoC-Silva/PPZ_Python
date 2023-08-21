nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')

if ' ' not in nome:
    space = 'Seu nome não possui espaços.'
else:
    space = 'Seu nome possui espaços'

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome de trás para a frente é "{nome[-1].upper()}{nome[-2:-(len(nome)+1):-1]}"')
    print(space)
    print(f'Seu nome possui {len(nome)} letras.')
    print(f'A primera letra do seu nome é {nome[0].upper()}.')
    print(f'A última letra do seu nome é {nome[-1].upper()}')
else:
    print('Não deixe campos vazios!')
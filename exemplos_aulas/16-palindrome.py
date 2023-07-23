'''
Verifique se uma palavra é palíndrome
'''
palavra:str = input('Palavra: ')
palindrome = palavra == palavra[::-1]
print('A palavra é palíndrome?')
print(palindrome)

#obs:Strings são imutáveis!
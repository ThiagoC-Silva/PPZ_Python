'''
Calcule quantas palavras possuem uma das letras “python” e que tenham 
mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
minúsculas e de remover antes os caracteres especiais.

texto: 
The Python Software Foundation and the global Python community 
welcome and encou rage participation by everyone. Our community 
is based on mutual respect, tolerance, and encouragement, and we 
are working to help each other live up to these principles. We want
our community to be more diverse: whoever you are, and whatever your 
background, we welcome you.
'''
texto = '''The Python Software Foundation and the global
   Python community  welcome and encourage participation
   by everyone Our community is based on mutual respect
   tolerance and encouragement and we are working to
   help each other live up to these principles We want
   our community to be more diverse: whoever you are and
   whatever your background we welcome you'''.lower().split()

quanti_palavras = 0
for palavra in texto:
    cont = 0
    while cont < len(palavra):
        if palavra[cont] in 'pythonPYTHON' and len(palavra)>=5:
            quanti_palavras = quanti_palavras + 1
            print(palavra)
            break
        cont = cont + 1

print(f'{quanti_palavras} palavras')
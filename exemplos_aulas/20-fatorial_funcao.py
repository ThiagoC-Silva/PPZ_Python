

def fat(fim):
    fatorial = 1
    cont = 2

    while cont <= fim:
        fatorial = fatorial * cont
        cont = cont + 1
    return fatorial

for i in range(6): print(fat(i))
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento 
de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a 
população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
'''

populaA = 80000 #crescimento anual 3%
populaB = 200000 #crecimento anual 1.5%
anos = 0

while populaB > populaA:
    populaA = populaA + (populaA*0.03)
    populaB = populaB + (populaB*0.015)
    anos = anos + 1

print(f'Anos necessários: {anos} anos')
tabu = 1
while tabu <= 10:
    print(f'Tabuada do {tabu}')
    n = 1
    while n <= 10:
        print(f'{tabu} x {n} = {tabu*n}')
        n = n + 1
    tabu = tabu + 1 
    print()
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,11))

for i in numeros:
    if i % 2 == 0:
        print(f'O numero {i} é par!')
    else:
        print(f'O numero {i} é impar!')
    
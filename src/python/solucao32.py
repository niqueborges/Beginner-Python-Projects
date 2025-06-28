numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda num: num ** 2

resultados = []
for i in numeros:
    resultados.append(quadrado(i))

print(f'Os quadrados dos numeros {numeros} são {resultados}')

def potencia(base, expoente=2):
    return base ** expoente

user_number = int(input('Digite o numero base: '))
user_exponente = input('Digite um expoente (default 2): ')

if user_exponente:
    print(f'O resultado é: {potencia(user_number, int(user_exponente))}')
else:
    print(f'O resultado é: {potencia(user_number)}')
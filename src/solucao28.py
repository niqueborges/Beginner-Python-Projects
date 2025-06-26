def dobrar(num):
    return num * 2

def quadrado(num):
    return dobrar(num) ** 2

user_number = int(input('Digite um número: '))
print(f'O quadrado do dobro do numero {user_number} é {quadrado(user_number)}')
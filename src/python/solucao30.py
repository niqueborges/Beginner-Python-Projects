# def multiplicar(num1, num2):
#     return num1 * num2

multiplicar = lambda num1, num2: num1 * num2

user_number1 = int(input('Digite o primeiro numero: '))
user_number2 = int(input('Digite o segundo numero: '))

print(f'A multiplicação de {user_number1} e {user_number2} é {multiplicar(user_number1, user_number2)}')
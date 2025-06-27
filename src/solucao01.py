print("Olá, mundo Python!")

entrada = input('Qual é o seu nome? ')
print('Seu nome é', entrada)

print('---')

# Exemplo de uso de if, elif e else

pontuacao = 91
if pontuacao <= 50:
    print('newba')
elif 50 < pontuacao <= 70:
    print = ('mediano')
elif 70 < pontuacao <= 90:
    print ('óia ele')
else:
    print('O escolhido')
    
print('---')

# Criando duas variaveis
first_name = 'Andre' # string
age = 39 # integer

print('Olá, menu nome é', first_name, 'e eu tenho', age, 'anos.')

print('---')

num1 = 10
num2 = 3.5

result = num1 / num2

print('O resultado da divisão é', result)

print('---')

first_name = input('Por favor, digite o seu nome: ') # String
age = int(input('Agora, digite a sua idade: ')) # Integer

print('Olá, {}! Você tem {} anos'.format(first_name, age))
print('Olá,', first_name, 'Você tem', age, 'anos')
print(f'Olá, {first_name}! Você tem {age} anos')

print('---')

# Perdir ao usuário que digite dois numeros
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

# Realizar os calculos matematicos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

# Imprimindo os resultados na console
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Exponenciação: {exponenciacao}')

print('---')

frutas = ['Maça', 'banana', 'manga', 'uva']

print(frutas)

print('---')




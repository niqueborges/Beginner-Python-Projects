"""
Operadores Relacionais
== > >= < >= !=
"""

print(2 == 2)
print(2 == 3)
print(2 != 2)
print(2 != 3)
print(2 > 2)
print(2 > 3)
print(2 < 2)
print(2 < 3)
print(2 >= 2)
print(2 >= 3)
print(2 <= 2)
print(2 <= 3)

num_1 = 2  # int
num_2 = '2'  # string
print(num_1, num_2)
print(num_1 == num_2)
print(num_1 != num_2)
# print(num_1 > num_2)  # TypeError: '>' not supported between instances of 'int' and 'str'
# print(num_1 >= num_2)
# print(num_1 <= num_2)

expressao = (num_1 == num_2)
expressao_1 = (num_1 != num_2)
# expressao_2 = (num_1 > num_2)  # TypeError: '>' not supported between instances of 'int' and 'str'
# expressao_3 = (num_1 >= num_2)  # TypeError: '>' not supported between instances of 'int' and 'str'
# expressao_4 = (num_1 <= num_2)  # TypeError: '>' not supported between instances of 'int' and 'str'
print(expressao)
print(expressao_1)
# print(expressao_2)
# print(expressao_3)
# print(expressao_4)

num_1 = 2
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

expressao = (num_1 == num_2)
expressao_1 = (num_1 != num_2)
expressao_2 = (num_1 > num_2)
expressao_3 = (num_1 >= num_2)
expressao_4 = (num_1 <= num_2)
print(expressao)
print(expressao_1)
print(expressao_2)
print(expressao_3)
print(expressao_4)

"""nome= input('Qual o seu nome? ')
idade = (int(input('Qual a sua idade? ')))

# Limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo')"""

nome = input('Qual o seu nome? ')
idade = (int(input('Qual a sua idade? ')))

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo')


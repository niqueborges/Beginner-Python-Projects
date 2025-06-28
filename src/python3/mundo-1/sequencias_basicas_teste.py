modo_teste = True  # Mude para False quando quiser usar input de verdade

print('Olá, Mundo!')
print('---')

# Boas-vindas com nome
if modo_teste:
    nome = "João da Silva"
else:
    nome = input('Qual é o seu nome? ')
print(f'Olá, {nome}! Prazer em te conhecer!')
print('---')

# Nome e salário
if modo_teste:
    nome_funcionario = "Maria do Carmo"
    salario = 1850.45
else:
    nome_funcionario = input('Nome do funcionário: ')
    salario = float(input('Salário: R$ '))
print(f'O funcionário {nome_funcionario} tem um salário de R$ {salario} em junho de 2025.')
print('---')

# Soma de dois inteiros
if modo_teste:
    num1 = 8
    num2 = 5
else:
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}.')
print('---')

# Média de duas notas
if modo_teste:
    nota1 = 7.5
    nota2 = 8.0
else:
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print(f'A média entre {nota1} e {nota2} é igual a {media:.2f}.')
print('---')

# Escreva um programa que mostre na tela a mensagem "Olá, Mundo!".

print('Olá, Mundo!')

print('---')

# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas:
# Ex: 
# Qual é o seu nome? João da Silva
# Olá, João da Silva! Prazer em te conhecer!

nome = input('Qual é o seu nome? ')
print(f'Olá, {nome}! Prazer em te conhecer!')

print('---')

# Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
# Ex:
# Nome do funcionário: Maria do Carmo
# Salário: R$ 1850,45
# O funcionário Maria do Carmo tem um salário de R$ 1850,45 em junho de 2025.

nome_funcionario = input('Nome do funcionário: ')
salario = float(input('Salário: R$ '))
print(f'O funcionário {nome_funcionario} tem um salário de R$ {salario} em junho de 2025.')


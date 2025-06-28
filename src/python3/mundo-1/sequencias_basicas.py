# Escreva um programa que mostre na tela a mensagem "Olá, Mundo!".

print('Olá, Mundo!')

print('---')

# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas:
# Ex: 
# Qual é o seu nome? João da Silva
# Olá, João da Silva! Prazer em te conhecer!

nome = (input('Qual é o seu nome? '))
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

print('---')

# Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles.
# Ex:
# Digite um valor: 8
# Digite outro valor: 5
# A soma entre 8 e 5 é igual a 13.

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}.')

print('---')

# Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
# Ex:
# Nota 1: 7.5
# Nota 2: 8.0   
# A média entre 7.5 e 8.0 é igual a 7.75.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print(f'A média entre {nota1} e {nota2} é igual a {media:.2f}.')

print('---')




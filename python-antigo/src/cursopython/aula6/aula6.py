"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Monique'
idade = 45
altura = 1.72
e_maior = idade > 18
peso = 83
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É Maior:', e_maior)
print('Peso:', peso)

print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc, '.')
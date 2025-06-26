"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa;
* Criar a variável com o ano atual (int);
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual);
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa);
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves).

Exibir: Luiz tem 32 anos, 1.80 de altura e pesa 80kg.
O imc de Luiz é 24.69.
Luiz nasceu em 1987.    
"""

nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80
ano_atual = 2025
data_nascimento = ano_atual - idade
IMC = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O imc de {nome} é {IMC:.2f}.')
print(f"{nome} nasceu em {data_nascimento}.")
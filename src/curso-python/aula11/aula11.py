"""
Operadores Lógicos
and, or, not
in e not in
"""

# (Verdadeiro E Verdadeiro) AND
# (Verdadeiro OR Falso ou Falso OR Verdadeiro) OR
#

"""a = 2
b = 3

if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

nome = 'Monique Borges.'

if 'o' in nome:
    print('Existe.')
else:
    print('Não existe.')"""


usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Monique'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')


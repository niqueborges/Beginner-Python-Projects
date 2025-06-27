# continue

while True:
    username = input('username? ')
    if username != 'neo':
        print('Nunca nem vi')
        continue
    senha = input('Qual a sua senha? ')
    if senha == '1234':
        print('Bem-vindo, {}'.format(username))
        print('Aceita um café? ')
        break
cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador')
cidade_usuario = input('Digite o nome da cidade: ')

if cidade_usuario in cidades:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')
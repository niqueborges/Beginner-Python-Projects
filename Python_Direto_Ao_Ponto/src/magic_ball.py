#

import random

# Gera números aletórios entre 0 e 5
guess = random.randint(0, 5)
input('Me faça uma pergunta: Vou concluir o livro em 2019? ')

if guess == 0:
    print('Sim, com certeza')
elif guess == 1:
    print('Parece bom')
elif guess == 2:
    print('Melhor não te dizer agora')
elif guess == 3:
    print('Não posso prever agora')
elif guess == 4:
    print('Não conte com isso')
elif guess == 5:
    print('Minhas fontes dizem não')
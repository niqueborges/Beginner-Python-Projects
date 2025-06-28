# Coleções -Listas, Tuplas, Dicionário
# [] - Listas - Mutáveis - Alteraveis
# () - Tuplas - Imutáveis - Não alteraveis
# {} - Dicionário - Mutáveis - Alteraveis

lista = [19, 35, 89, 76, 98, 16, 54, 12]
lista_strings = ['maca', 'banana', 'laranja']
lista_mista = [19, 'maca', 35, 'banana', 89, 'laranja']
lista_vazia = []
lista_aninhada = [[19, 35, 89], [76, 98, 16], [54, 12]]

# Funções
lista_strings.append('uva')  # Adiciona 'uva' ao final da lista
lista_strings.insert(1, 'pera')  # Insere 'pera' na posição 1
lista_strings.remove('banana')  # Remove 'banana' da lista
#lista_strings.clear()  # Limpa a lista
print(lista_strings)  # Imprime a lista
print(lista_mista)
print(lista_vazia)  # Imprime a lista vazia
print(lista_aninhada)  # Imprime a lista aninhada

print(len(lista))  # Imprime o tamanho da lista
print(lista[0])  # Imprime o primeiro elemento da lista 
print(lista[-1])  # Imprime o último elemento da lista
print(lista[1:4])  # Imprime os elementos do índice 1 ao 3 (exclusivo)
print(lista[1:])  # Imprime os elementos do índice 1 até o final    
print(max(lista))  # Imprime o maior elemento da lista
print(min(lista))  # Imprime o menor elemento da lista
print(sum(lista))  # Imprime a soma de todos os elementos da lista

# Slicing - Indexação 
print(lista[0])  # Imprime o primeiro elemento da lista
print(lista[-1])  # Imprime o último elemento da lista

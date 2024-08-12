# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com as informações abaixo:

Lista1= Funcionários que tem carro e trabalham à noite
Lista2= Funcionários que tem carro e trabalham de dia
Lista3= Funcionários que não tem carro

'''
funcionarios = ['Ana', 'João', 'Maria', 'José', 'Carlos', 'Mariana', 'Paulo', 'Pedro', 'Luana', 'Luiz']
turno_dia = ['Ana', 'João', 'Maria', 'José', 'Carlos']
turno_noite = ['Mariana', 'Paulo', 'Pedro', 'Luana', 'Luiz']
tem_carro = ['Ana', 'João', 'Maria', 'José', 'Carlos', 'Mariana', 'Paulo', 'Pedro']


#Lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A lista será')
print(lista)

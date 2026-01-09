#Funções para sortear e somar
#minha resolução
from random import randint as ran
numeros = []
def sorteia():
    print('Sorteando 5 valoresda lista:', end=' ')
    while len(numeros) < 5:
        n = ran(1, 10)
        # este if é para n repetir numeros
        if n not in numeros:
            numeros.append(n)
            print(n, end=' ')
    print('Pronto !')
def somaPar():
    n = 0
    for i in numeros:
        if i % 2 == 0:
            n += i
    print(f'Somando os valores pares de {numeros}, temos: {n} ')            
sorteia()
somaPar()

#Resolução do curso
'''
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('Pronto!')
def somapar(lista):
    soma = 0
    for valor in lista 
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = list()
sorteia(numeros)
somapar(numeros)
'''
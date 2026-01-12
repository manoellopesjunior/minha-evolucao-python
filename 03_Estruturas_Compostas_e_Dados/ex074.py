from random import randint as r
lista = []
for c in range(5):
    lista.append(r(1, 100))
maior = lista[0]
menor = lista[0]
for n in lista:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(lista)
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')


# outro modo eu ja adiciono o randint ja dentro da tupla, mostro os numeros com print e nos proximos prints
# uso max e min para achar o maior e menor valor dentro da tupla, um código com menos linhas e mais simples
# numeros = (r(1,100), r(1,100), r(1,100), r(1,100), r(1,100))
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#   print(f'{n} ', end='')
# print(f'\nO maior valor sorteado foi {max(lista)}')
# print(f'O menor valor sorteado foi {min(lista)}')

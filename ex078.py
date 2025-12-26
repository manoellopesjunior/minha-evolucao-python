lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
max = max(lista)
min = min(lista)
print('=-' * 20)
print(f'Voçê digitou os valores {lista}')
print(f'O maior valor digitado foi {max} e está na posição: ', end='')
for i, v in enumerate(lista):
    if v == max:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor digitado foi {min} e está na posição: ', end='')
for i, v in enumerate(lista):
    if v == min:
        print(f'{i+1}...', end='')
print()


'''lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Voçê digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
posição_maior = []
posição_menor = []

for pos, valor in enumerate(lista):
    if valor == maior:
        posição_maior.append(pos+1)
    if valor == menor:
        posição_menor.append(pos+1)

if len(posição_maior) == 1:
    print(f'O maior valor foi {maior} e está na posição {posição_maior[0]}')
else:
    print(f'O maior valor foi {maior} e estão nas posições ', end='')
    print(' e '.join(map(str, posição_maior)))

if len(posição_menor) == 1:
    print(f'O menor valor foi {menor} e está na posição {posição_menor[0]}')
else:
    print(f'O menor valor foi {menor} e estão nas posições ', end='')
    print(' e '.join(map(str, posição_menor)))'''
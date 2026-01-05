lista = []
pessoa = []
maior = menor = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    continuar = input('Deseja continuar ? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar ? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break


print('=' * 40)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}Kg. peso de ', end='')
for p in lista:
    if p[0] == menor:
        print(f'[{p[0]}]', end='')
print()
        

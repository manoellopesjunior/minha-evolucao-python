lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]

    while continuar not in 'SN':
        continuar = input('Digite [S/N] para continuar ou parar!!! : ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'Foram digitados {len(lista)} numeros!!!')
print(f'A lista em ordem decrescente:{sorted(lista, reverse=True)}')
if 5 in lista:
    print('O numero 5 se encontra na lista')
else:
    print('O numero 5 não se encontra na lista')


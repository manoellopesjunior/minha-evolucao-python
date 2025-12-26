
lista = (
    ['Lápis', 1.75],
    ['Borracha', 2.00],
    ['Caderno', 15.90],
    ['Estojo', 25.00],
    ['Transferidor', 4.20],
    ['Compasso', 9.99],
    ['Mochila', 120.32],
    ['Canetas', 22.30],
    ['Livro', 34.90]
)
print('-' * 58)
print(f'{'LISTAGEM DE PREÇOS':^58}')
print('-' * 58)
for nome, preço in lista:
    print(f'{nome:.<45} R$: {preço:>7.2f}')
print('-' * 58)


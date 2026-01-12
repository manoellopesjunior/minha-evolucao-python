matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = linha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para [{l}, {c}]: '))
        
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
for l in range(0, 3):
    coluna += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        linha = matriz[1][c]
    elif matriz[1][c] > linha:
        linha = matriz[1][c]
print('=' * 30)

print(f'A soma de todos os valores pares digitados é : {pares}')
print(f'A soma dos valores da terceira coluna é : {coluna}')
print(f'O maior valor da segunda linha é : {linha}')

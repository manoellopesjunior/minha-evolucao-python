lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = input('Deseja continuar [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Digite apenas [S/N] para continuar ou parar: ').strip().upper()[0]
    if continuar == 'N':
        break

for item in lista:
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)

print(f'Lista completa: {lista}')
print(f'Lista apenas numeros pares: {lista_par}')
print(f'Lista apenas numeros impares: {lista_impar}')

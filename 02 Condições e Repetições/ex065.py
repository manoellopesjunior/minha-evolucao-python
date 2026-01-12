total = 0
contador = 0

while True:
    numero = int(input('Digite um número: '))
    total += numero
    contador += 1

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

media = total / contador
print(f'Você digitou {contador} números e a média foi {media:.2f}')


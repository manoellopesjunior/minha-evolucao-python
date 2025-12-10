'''n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''

'''from math import factorial
print('Fatorial de 5!')
f = factorial(5)
for c in range(5, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f'{f}')'''

'''n = int(input('Digite um número e direi seu fatorial: '))
acumulador = 1
contador = n
while contador > 0:
    acumulador = acumulador * contador
    contador -= 1
print(acumulador)'''
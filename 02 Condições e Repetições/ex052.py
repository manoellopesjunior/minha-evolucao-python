n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c ==0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {tot} vezes.')
#if para saber quantas vezes foi divisivel , se mais q 2 não é primo
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


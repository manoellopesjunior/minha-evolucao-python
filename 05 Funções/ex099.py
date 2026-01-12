#minha solução usando a biblioteca random
from random import randint
def contador(qtd):
    numeros = []
    print('=-' * 40)
    print('Analisando os valores passados...')
    for c in range(qtd):
        n = randint(1, 100)
        numeros.append(n)
        print(n, end=' ')
    if qtd == 0:
        print(f'Foram informador {len(numeros)} valores ao todo')
        print(f'O maior valor informados foi {max(numeros)}.')

    print(f'Foram informador {len(numeros)} valores ao todo')
    print(f'O maior valor informados foi {max(numeros)}.')

qtd = randint(1,10)  
for c in range(qtd):
    contador(randint(1, 10))
print('=-' * 40)

'''# exemplo da aula
from time import sleep
def maior(*num):
    cont = maior = 0
    print('-='* 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valors ao todo.')
    print(f'O maior valor informado foi {maior}.')
#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''

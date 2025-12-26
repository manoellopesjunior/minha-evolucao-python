'''num =   ((int(input('Digite um número: ))),
            (int(input('Digite outro número: ))),
            (int(input('Digite mais um número: ))),
            (int(input('Digite o útimo número: ))))    
    print(f'Voçê digitou os numeros {num}')    
    print(f'O número 9 apareceu {num.count(9)} vezes.)
    if 3 in num:
        print(f'O primeiro valor 3 foi digitado na {num.indes(3)+1}° posição.)
    else:
        print('O número 3 não foi digitado.)
    print('Os numeros pares digitados foram', end='')
    for n in num:
        if num % 2 == 0:
            print(n, end=' ')'''

'''O primeiro modo é mais simples como no exercicio passado , ja adicionando os valores dentro da tupla e não
adicionando eles um por um depois usando o laço for, após isso eu imprimo os numeros , conto os numero 9 usando .count()
uso if para saber se o numero 3 foi digitado e por ultimo mostro os numeros para um por um usando mais uma vez o laço for.'''

lista = []
cont =  0
pares = []
p = 0
for c in range(1, 5):
    n = int(input('Digite um número: '))
    lista.append(n)
for n in lista:
    if n == 9:
        cont += 1
for par in lista:
        if par % 2 == 0:
            p += 1
            pares.append(par)
print(lista)
for n in lista:
    if 9 in lista:
        print(f'O número 9 apareceu {cont} vezes')
    else:
        print('O npumero 9 não foi digitado')
    if 3 in lista:
        print(f'O número 3 foi digitado na {lista.index(3)+1}° posição')
    else:
        print('O número 3 não foi digitado')

    if p == 0:
        print('Não foi digitado nenhum numero par')
    else:
        print(f'Os numeros pares foram {pares}')
    break

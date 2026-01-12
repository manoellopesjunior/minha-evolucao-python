'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
loop = False
while not loop:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    opcao = input('Qual operação deseja realizar?: ')

    if opcao == '1':
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opcao == '2':
        mult = n1 * n2
        print(f'A multiplicação de {n1} x {n2} = {mult}')
    elif opcao == '3':
        if n1 == n2:
            print('O numeros são iguais')
        elif n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        else:
            print(f'O numero {n2} é maior que {n1}')
    elif opcao == '4':
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif opcao == '5':
        loop = True
    else:
        print('Opção Invalida, tente novamente.')'''
from time import sleep
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} = {mult}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida, tente novamente.')
    sleep(2)
print('Fim do programa! Volte sempre!')

lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso...')
        
    else:
        print('Número duplicado! Não vou adicionar...')
    
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Opção Inválida. Digite [S/N] para continuar ou parar: ').strip().upper()[0]
    if continuar == 'N':
            break
print('=' * 20)
print(lista)
print('=' * 20)
lista.sort()
print(f'Valores em ordem crescente {lista}')
print('=' * 20)


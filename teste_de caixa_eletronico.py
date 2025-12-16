saldo_inicial = 0
extrato = []

while True:
    print('Menu:')
    print('1 - Depositar')  
    print('2 - Sacar')
    print('3 - Extrato')
    print('4 - Ver saldo')
    print('5 - Sair')
    
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida. Por favor, escolha um número entre 1 e 5.')
        continue
    
    if opcao == 1:
        while True:
            try:
                valor = float(input('Digite o valor a ser depositado: '))
                if valor <= 0:
                    print('Valor inválido. O depósito deve ser maior que zero.')
                    continue
                saldo_inicial += valor
                extrato.append(f'Depósito: R$ {valor:.2f}')
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
                break
            except ValueError:
                print('Entrada inválida. Por favor, insira um número válido.')

    elif opcao == 2:
            if saldo_inicial <= 0:
                print('Saldo insificiente para saque:')
            else:
                try:
                    valor = float(input('Digite o valor a ser sacado: '))
                    if valor <= 0:
                        print('Valor inválido. O saque deve ser maior que zero.')
                    elif valor > saldo_inicial:
                        print('Saldo insuficiente para o saque.')
                    else:
                        saldo_inicial -= valor
                        extrato.append(f'Saque: R$ {valor:.2f}')
                        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
                except ValueError:
                    print('Entrada inválida. Por favor, insira um número válido.')
    elif opcao == 3:
        print('Extrato:')
        if not extrato:
            print('Nenhuma movimentação realizada.')
        else:
            for item in extrato:
                print(item)
        print(f'Saldo atual: R$ {saldo_inicial:.2f}')

    elif opcao == 4:
        print('-'*30)
        print(f'Seu saldo atual é: R$ {saldo_inicial:.2f}')
        print('-'*30)

    elif opcao == 5:
        print('Saindo do sistema. Obrigado por usar nosso caixa eletrônico!')
        break

    else:
        print('Opção inválida. Por favor, escolha um número entre 1 e 5.')
    



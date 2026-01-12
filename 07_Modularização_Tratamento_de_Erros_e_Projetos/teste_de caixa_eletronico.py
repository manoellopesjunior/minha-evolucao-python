"""
Caixa Eletrônico simples.

Permite ao usuário realizar depósitos, saques, consultar extrato e saldo.

"""

# Saldo inicial do usuário
saldo_inicial = 0

# Lista que guarda o histórico de transações
extrato = []

# Loop principal do programa
while True:
    # Exibe o menu de opções
    print('Menu:')
    print('1 - Depositar')  
    print('2 - Sacar')
    print('3 - Extrato')
    print('4 - Ver saldo')
    print('5 - Sair')
    
    # Solicita a opção do usuário e trata entradas inválidas
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida. Por favor, escolha um número entre 1 e 5.')
        continue
    
    # Depósito
    if opcao == 1:
        while True:
            try:
                valor = float(input('Digite o valor a ser depositado: '))
                if valor <= 0:
                    print('Valor inválido. O depósito deve ser maior que zero.')
                    continue
                saldo_inicial += valor
                extrato.append(f'Depósito: R$ {valor:.2f}')  # Registra o depósito no extrato
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
                break
            except ValueError:
                print('Entrada inválida. Por favor, insira um número válido.')

    # Saque
    elif opcao == 2:
        if saldo_inicial <= 0:
            print('Saldo insuficiente para saque.')
        else:
            try:
                valor = float(input('Digite o valor a ser sacado: '))
                if valor <= 0:
                    print('Valor inválido. O saque deve ser maior que zero.')
                elif valor > saldo_inicial:
                    print('Saldo insuficiente para o saque.')
                else:
                    saldo_inicial -= valor
                    extrato.append(f'Saque: R$ {valor:.2f}')  # Registra o saque no extrato
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            except ValueError:
                print('Entrada inválida. Por favor, insira um número válido.')

    # Exibe extrato
    elif opcao == 3:
        print('Extrato:')
        if not extrato:
            print('Nenhuma movimentação realizada.')
        else:
            for item in extrato:
                print(item)
        print(f'Saldo atual: R$ {saldo_inicial:.2f}')

    # Exibe saldo
    elif opcao == 4:
        print('-'*30)
        print(f'Seu saldo atual é: R$ {saldo_inicial:.2f}')
        print('-'*30)

    # Sai do programa
    elif opcao == 5:
        print('Saindo do sistema. Obrigado por usar nosso caixa eletrônico!')
        break

    # Opção inválida
    else:
        print('Opção inválida. Por favor, escolha um número entre 1 e 5.')

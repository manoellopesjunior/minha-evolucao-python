import os

pass

if not os.path.exists('Cadastro de Pessoas.txt'): 
    with open('Cadastro de Pessoas.txt', 'a') as arquivo:
        pass
    print('Cadastro de Pessoas.txt criado com sucesso!'.center(50))
else:
     print('Arquivo encontrado. Dados carregados.'.center(50))

def cadastrados():
    linha()
    print('PESSOAS CADASTRADAS'.center(50))
    linha()
    with open('Cadastro de Pessoas.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
    if not conteudo:
        print('Nenhuma pessoa cadastrada ainda.'.center(50))
    else:
        for linha_txt in conteudo:
            print(linha_txt.strip())

def linha():
    print('-' * 50)

def opição(num):
    linha()
    print(f'Opção {num}'.center(50))
    linha()

while True:
    linha()
    print('MENU PRINCIPAL'.center(50))
    linha()
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    linha()
    try:
        opc = int(input('Sua Opção: '))
        if opc == 1:
            opição(opc)
            cadastrados()

        elif opc == 2:
            opição(opc)
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            print('Pessoa cadastrada com sucesso!'.center(50))

            with open('Cadastro de Pessoas.txt', 'a') as arquivo:
                 arquivo.write(f'{nome:<30}{idade:>3} anos\n')

        elif opc == 3:
            opição(opc)
            print('Saindo... Volte sempre!'.center(50))
            break

        else:
             print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[0m')
        
    except ValueError:
            print('\033[31mERRO: digite uma opção válida\033[0m')
    


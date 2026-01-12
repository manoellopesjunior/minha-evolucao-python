"""
Sistema de Cadastro de Pessoas

Permite cadastrar novas pessoas em um arquivo de texto, listar pessoas cadastradas e sair do sistema.

Autor: Manoel Lopes
Data: 2026-01-12
"""

import os

# Verifica se o arquivo 'Cadastro de Pessoas.txt' existe
# Se não existir, cria o arquivo vazio
if not os.path.exists('Cadastro de Pessoas.txt'): 
    with open('Cadastro de Pessoas.txt', 'a') as arquivo:
        pass
    print('Cadastro de Pessoas.txt criado com sucesso!'.center(50))
else:
    print('Arquivo encontrado. Dados carregados.'.center(50))

# -----------------------------
# Funções do sistema
# -----------------------------

def linha():
    """
    Imprime uma linha separadora de 50 caracteres.
    """
    print('-' * 50)

def opicao(num):
    """
    Exibe a opção escolhida pelo usuário no menu.

    Parâmetros:
    num (int): número da opção selecionada
    """
    linha()
    print(f'Opção {num}'.center(50))
    linha()

def cadastrados():
    """
    Exibe todas as pessoas cadastradas no arquivo.
    """
    linha()
    print('PESSOAS CADASTRADAS'.center(50))
    linha()
    with open('Cadastro de Pessoas.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
    if not conteudo:
        print('Nenhuma pessoa cadastrada ainda.'.center(50))
    else:
        for linha_txt in conteudo:
            print(linha_txt.strip())  # Remove espaços extras no final da linha

# -----------------------------
# Loop principal do sistema
# -----------------------------

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
            opicao(opc)
            cadastrados()

        elif opc == 2:
            opicao(opc)
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            print('Pessoa cadastrada com sucesso!'.center(50))

            # Escreve os dados da nova pessoa no arquivo
            with open('Cadastro de Pessoas.txt', 'a') as arquivo:
                arquivo.write(f'{nome:<30}{idade:>3} anos\n')

        elif opc == 3:
            opicao(opc)
            print('Saindo... Volte sempre!'.center(50))
            break

        else:
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[0m')
    
    except ValueError:
        print(f'\033[31mERRO! Entrada inválida. Digite um número inteiro\033[0m')

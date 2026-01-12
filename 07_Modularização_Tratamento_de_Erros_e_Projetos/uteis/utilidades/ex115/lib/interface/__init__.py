def linha():
    """
    Imprime uma linha separadora de 50 caracteres.
    """
    print('-' * 50)


def cabecalho(txt):
    """
    Exibe um cabeçalho formatado com o texto centralizado
    e linhas acima e abaixo.

    Parâmetros:
        txt (str): texto que será exibido no cabeçalho.
    """
    linha()
    print(txt.center(50))
    linha()


def leiaint(msg):
    """
    Lê um número inteiro digitado pelo usuário.

    A função:
    - Permanece em loop até que o usuário digite um valor inteiro válido.
    - Usa try/except para capturar entradas inválidas:
        * ValueError ou TypeError: exibe mensagem de erro e repete o pedido.
        * KeyboardInterrupt: retorna 0 e informa que o usuário cancelou.
    - Retorna o número inteiro digitado corretamente.

    Parâmetros:
        msg (str): mensagem exibida para o usuário ao solicitar o número.

    Retorno:
        int: número inteiro digitado pelo usuário ou 0 se cancelado.
    """
    while True:  
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


def menu(lista):
    """
    Exibe um menu de opções numeradas baseado em uma lista de textos.

    A função:
    - Exibe o cabeçalho "MENU PRINCIPAL".
    - Lista as opções com cores diferenciadas.
    - Solicita a opção do usuário usando a função `leiaint`.
    - Retorna a opção escolhida.

    Parâmetros:
        lista (list): lista de strings representando as opções do menu.

    Retorno:
        int: número da opção escolhida pelo usuário.
    """
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')  # formata cores das opções
        c += 1
    linha()
    opc = leiaint('\033[32mSua Opção: \033[m')  # lê opção do usuário
    return opc

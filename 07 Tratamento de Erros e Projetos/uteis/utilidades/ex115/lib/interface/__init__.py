def linha():
    print('-' * 50)

def cabecalho(txt):
    linha()
    print(txt.center(50))
    linha()

def leiaint(msg):
    """
    Lê um número inteiro digitado pelo usuário.

    Funcionamento:
    - Fica em um loop infinito usando `while True`, até que o usuário digite um valor válido.
    - Usa um bloco `try/except`:
        * `try` tenta converter o valor digitado para inteiro com `int()`.
        * Se a conversão funcionar, a função retorna o número e encerra.
        * Se ocorrer um erro (por exemplo, o usuário digitar letras), o `except ValueError`
          exibe uma mensagem informando que o valor é inválido e repete o pedido.

    Retorno:
        int: O número inteiro digitado corretamente pelo usuário.
    """
    while True:  
        try:
            valor = int(input(msg)) 
            
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc

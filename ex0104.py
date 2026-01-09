def leiaint():
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
            n = int(input('Digite um número: ')) 
            return n
        except ValueError:
            print(f'\033[31mERRO! Digite um número válido\033[0m')


n = leiaint()
print(f'Você acabou de digitar o número {n}')

'''
def leiaint(msg)
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31mERRO! Digite um número válido\033[0m')
        if ok:
            break
    reutn valor

n = leiaint('Digite un numero:')
print(f'voce acabou de digitar um numero {n}')'''
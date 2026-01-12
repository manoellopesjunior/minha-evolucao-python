def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}" é um preço inválido"\033[m')
        else:
            valido = True
            return(float(entrada))
        

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
            return valor
        except ValueError:
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[0m')


def leiareal(msg):
    while True:
        try:
            valor = input(msg).replace(',', '.') # troca virgula por ponto
            return float(valor)
        except ValueError:
            print(f'\033[31mERRO! Por favor, digite um número real válido\033[0m')

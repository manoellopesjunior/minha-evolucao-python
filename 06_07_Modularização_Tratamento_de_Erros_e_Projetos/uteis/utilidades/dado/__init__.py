def leiadinheiro(msg):
    """
    Lê um valor monetário digitado pelo usuário e retorna como float.

    Funciona substituindo vírgulas por pontos, removendo espaços extras
    e garantindo que a entrada seja um número válido. Continua pedindo
    até que o usuário digite corretamente.

    Parâmetros:
        msg (str): mensagem exibida para o usuário.

    Retorno:
        float: valor monetário digitado corretamente.
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()  # remove espaços e troca vírgula por ponto
        if entrada.isalpha() or entrada == '':  # verifica se não é número
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    """
    Lê um número inteiro digitado pelo usuário.

    Continua pedindo até que seja digitado um valor inteiro válido.
    Usa try/except para capturar entradas inválidas.

    Parâmetros:
        msg (str): mensagem exibida para o usuário.

    Retorno:
        int: número inteiro digitado corretamente.
    """
    while True:  
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print(f'\033[31mERRO! Por favor, digite um número inteiro válido\033[0m')


def leiareal(msg):
    """
    Lê um número real (float) digitado pelo usuário.

    Substitui vírgulas por pontos e continua pedindo até que a entrada
    seja um número real válido.

    Parâmetros:
        msg (str): mensagem exibida para o usuário.

    Retorno:
        float: número real digitado corretamente.
    """
    while True:
        try:
            valor = input(msg).replace(',', '.')  # troca vírgula por ponto
            return float(valor)
        except ValueError:
            print(f'\033[31mERRO! Por favor, digite um número real válido\033[0m')

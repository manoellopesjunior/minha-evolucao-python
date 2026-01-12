def aumentar(valor=0, porcentagem=0, formato=False):
    """
    Aumenta o valor em uma determinada porcentagem.

    Parâmetros:
        valor (float): valor inicial. Padrão 0.
        porcentagem (float): percentual de aumento. Padrão 0.
        formato (bool): se True, retorna o valor formatado como moeda. Padrão False.

    Retorno:
        float ou str: valor aumentado, formatado ou não dependendo de `formato`.
    """
    res = valor + (valor * porcentagem / 100)
    return res if not formato else moeda(res)


def diminuir(valor=0, porcentagem=0, formato=False):
    """
    Diminui o valor em uma determinada porcentagem.

    Parâmetros:
        valor (float): valor inicial. Padrão 0.
        porcentagem (float): percentual de redução. Padrão 0.
        formato (bool): se True, retorna o valor formatado como moeda. Padrão False.

    Retorno:
        float ou str: valor reduzido, formatado ou não dependendo de `formato`.
    """
    res = valor - (valor * porcentagem / 100)
    return res if not formato else moeda(res)


def dobro(valor=0, formato=False):
    """
    Calcula o dobro do valor.

    Parâmetros:
        valor (float): valor inicial. Padrão 0.
        formato (bool): se True, retorna o valor formatado como moeda. Padrão False.

    Retorno:
        float ou str: dobro do valor, formatado ou não dependendo de `formato`.
    """
    res = valor * 2
    return res if not formato else moeda(res)


def metade(valor=0, formato=False):
    """
    Calcula a metade do valor.

    Parâmetros:
        valor (float): valor inicial. Padrão 0.
        formato (bool): se True, retorna o valor formatado como moeda. Padrão False.

    Retorno:
        float ou str: metade do valor, formatado ou não dependendo de `formato`.
    """
    res = valor / 2
    return res if not formato else moeda(res)


def moeda(valor=0, moeda='R$'):
    """
    Formata um valor numérico como moeda brasileira.

    Parâmetros:
        valor (float): valor a ser formatado. Padrão 0.
        moeda (str): símbolo da moeda. Padrão 'R$'.

    Retorno:
        str: valor formatado como moeda (ex: R$12,50).
    """
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor=0, taxa_aumento=10, taxa_redução=5):
    """
    Exibe um resumo financeiro do valor, incluindo:
    - Preço analisado
    - Dobro do valor
    - Valor com aumento
    - Valor com redução

    Parâmetros:
        valor (float): valor base para análise. Padrão 0.
        taxa_aumento (float): percentual de aumento. Padrão 10.
        taxa_redução (float): percentual de redução. Padrão 5.

    Retorno:
        None
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(valor, taxa_aumento, True)}')
    print(f'{taxa_redução}% de redução: \t{diminuir(valor, taxa_redução, True)}')
    print('-' * 30)

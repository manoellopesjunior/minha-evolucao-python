def aumentar(valor = 0, porcentagem = 0, formato=False):
    res= valor + (valor * porcentagem / 100)
    return res if formato is False else moeda(res)

def metade(valor = 0, formato = False):
    res = valor / 2 
    return res if formato is False else moeda(res)

def dobro(valor = 0, formato = False):
    res = valor * 2 
    return res if formato is False else moeda(res)

def diminuir(valor = 0, porcentagem = 0, formato = False):
    res = valor - (valor * porcentagem / 100)
    return res if formato is False else moeda(res)


def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:>.2f}'.replace('.',',')

def resumo(valor = 0, taxa_aumento = 10, taxa_redução = 5):
    print('-' * 30) 
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30) 
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor, True)}')
    print(f'{taxa_aumento}% de aumeno: \t\t{aumentar(valor, taxa_aumento, True)}')
    print(f'{taxa_redução}% de redução: \t{diminuir(valor, taxa_redução, True)}')
    print('-' * 30)
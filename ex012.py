p = float(input('Digite o preço do produto: R$'))
n = p - (p * 5 / 100)


print('O preço era R${:.2f}, com 5% de desconto fica R${:.2f}'.format(p, n))

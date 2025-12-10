k = float(input('quilometragem percorrido: '))
d = int(input('Dias alugados: '))

km = k * 0.15
dia = d * 60

print('Voce percorreu {}Km a R$0,15 e usou {} dias a R$60'.format(k, d))
print('Voce pagará um total de R${:.2f}'.format(km + dia))

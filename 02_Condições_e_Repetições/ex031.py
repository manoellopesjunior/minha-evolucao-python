k = int(input('Qual a distancia da viagem?: '))
if k <= 200:
    p = k * 0.50
    print('Sua viagem é curta.')
    print('O valor da sua passagem é R${:.2f}'.format(p))
else:
    v = k * 0.45
    print('Sua viagem é longa')
    print('O valor da sua passagem é R${:.2f}'.format(v))

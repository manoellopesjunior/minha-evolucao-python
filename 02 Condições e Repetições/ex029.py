v = int(input('Qual a sua velocidade atual? :  '))
if v > 80:
    print('Você ultrapassou o limite de 80Km/h')
    print('Você foi multado!')
    multa = (v - 80) * 7
    print('Sua multa é de R$ {:.2f}'.format(multa))

else:
    print('Você está dentro do limite de 80Km/h')
    print('Boa Viagem!!!')

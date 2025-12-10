n1 = float(input('primeiro segmento: '))
n2 = float(input('segundo segmento: '))
n3 = float(input('terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2  == n3:
        print('Esses segmentos acima pordem formar um triangulo EQUILATERO')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Esses segmentos acima pordem formar um triangulo ESCALENO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Esses segmentos acima pordem formar um triangulo ISÓCELES')

else:
    print('Esses segmentos NÃO PODE FORMAR TRIANGULO')

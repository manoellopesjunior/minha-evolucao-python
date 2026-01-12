print('-=' * 20)
print('ANALISADOR DE TRIANGULOS')
print('-=' * 20)
n1 = float(input('primeiro segmento: '))
n2 = float(input('segundo segmento: '))
n3 = float(input('terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos PODEM FORMAR TRIANGULO')
else:
    print('Esses segmentos NÃO PODE FORMAR TRIANGULO')

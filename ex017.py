#esse modo achamos a raiz quadrada usando 'sqrt'
'''from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjascente: '))
r = sqrt( co ** 2 + ca ** 2 )
print('O comprimento da hipotenusa é: {:.2f}'.format(r))'''

#outro método é: usando 'hypot' que ja acha a hipotenusa sem achar a raiz quadrada
'''from math import hypot
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))'''

#maneira matematica de achar a hi achando a reiz quadrada

co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa é {:.2f}'.format(hi))

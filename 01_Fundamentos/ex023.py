# os dois modos dão certo

'''n = input('Ditite um número de 0 a 9999: ').zfill(4)
lista = list(n)
print('unidade: ',lista[3])
print('dezena: ',lista[2])
print('centena: ',lista[1])
print('milhar: ',lista[0])'''

num = int(input('informe um numero até 9999: '))
u = num //1 % 10
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10
print('analisando o numero {}'.format(num))
print('unidade: {} ...'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

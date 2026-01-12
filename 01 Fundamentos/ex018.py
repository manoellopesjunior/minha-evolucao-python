# esse método é errado pq temos que usar tambem o radiano para convertermos o (x) de seno cosseno e tangente
'''import math
a = float(input('Digite o valor de um angulo: '))
seno = math.sin(a)
coseno = math.cos(a)
tan = math.tan(a)
print('O seno é: {:.2f}\nO coseno é: {:.2f}\nA tangente é: {:.2f}'. format(seno, coseno, tan ))'''

from math import radians, sin, cos, tan

a = float(input('Digite o valor do ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O angulo de {} tem o Seno de {:.2f}'.format(a, s))
print('O angulo de {} ten o cosseno de {:.2f}'.format(a, c))
print('O angulo de {} tem a tangente de {:.2f}'.format(a, t))

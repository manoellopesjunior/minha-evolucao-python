'''from sympy import fibonacci as fib

n = int(input('Quantos termos você quer mostrar? '))
contador = 0

while contador < n:
    print(f'{fib(contador)} -> ', end='')
    contador += 1

print('FIM')'''

print('Termos de uma sequencia de FIBONACCI')
n = int(input('Quantos termos voce quer mostar?: '))

t1 = 0
t2 = 1
contador = 3
while contador < n:
    print(f'{t1} -> ', end='')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador = contador + 1
print('FIM')



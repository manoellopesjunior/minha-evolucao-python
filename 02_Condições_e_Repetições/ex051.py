print('=' * 30)
print('10 TERMOS DE UMA PA'.center(30))
print('=' * 30)

p = int(input('prieiro termo: '))
r = int(input('Razão: '))
d = p + (11 - 1 ) * r
for c in range(p, d, r):
    print(c, end=' -> ')
print('Acabou')

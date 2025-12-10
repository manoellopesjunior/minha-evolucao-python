print('=-' * 20)
s1 = float(input('Qual o valor do seu salario ? R$:'))
print('=-' * 20)
print()
if s1 <= 1250:
    ns = s1 + (s1 * 15 / 100)

else:
    ns = s1 + (s1 * 10 / 100)
print('Quam ganhava R${:.2f} passar a ganhar R${:.2f}'.format(s1, ns))

c = float(input('Valor da casa: R$ '))
s = float(input('Insira seu salário: R$ '))
a = int(input('Deseja pagar em quantos anos?: '))
p =  c / (a * 12)
m = s * 30 / 100
print(f'Para pagar um casa deR${c:.2f} em {a:.2f} anos')
print(f'A prestação sera de R${p:.2f}')
if p <= m:
    print('empréstimo pode ser concecido!')
else:
    print('Empréstimo Negado')

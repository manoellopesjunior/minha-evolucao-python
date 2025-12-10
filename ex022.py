'''nome = (input('Digite seu nome completo: '))
qnt = len(nome.replace(' ', ''))
div = nome.split()

print()
print('Seu nome em Maiúsculo:')
print(nome.upper())
print('Seu nome em Minúsculo:')
print(nome.lower())
print('Quantas letras tem o seu nome?')
print(qnt)
print('Quantas letras tem seu primeiro nome?')
print(len(div[0]))'''


nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculo é : {}'.format(nome.upper()))
print('Seu nome em minusculo é : {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

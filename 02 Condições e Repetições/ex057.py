'''sexo = 0
while sexo != 'M' and sexo != 'F':
    print('Digite um valor valido')
    sexo = input('Qual o seu sexo [M/F]: ').strip().upper()
    if sexo == 'M':
        print('Masculino')
    if sexo == 'F':
        print('Feminino')
print('Fim')'''

sexo =str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, Por favor , informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')

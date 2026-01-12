lista = ['Palmeiras','Flamengo','Atlético Mineiro','Grêmio','Botafogo','Red Bull Bragantino','Fluminense',
'Athletico Paranaense','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco da Gama',
'Bahia','Vitória','Criciúma','Juventude','Atlético Goianiense']

print('-='*20)
print(f'Lista de times do Brasileirão: {lista}')
print('-='*20)
print(f'Os 5 primeiros times são: {lista[0:5]}')
print('-='*20)
print(f'Os 4 últimos times são: {lista[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-='*20)
print(f'A posição do São Paulo na tabela é: {lista.index("São Paulo")+1}º lugar')
print('-='*20)


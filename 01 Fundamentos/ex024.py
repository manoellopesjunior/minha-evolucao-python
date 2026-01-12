'''cd = input('Qual o nome da sua cidade: ')
if cd[:5].lower() == 'santo':
    print('Sua cidade tem Santo no começo')
else:
    print('Sua cidade não tem Santo no começo')'''

cid = str(input('Qual o nome da sua cidade: ')).strip()
print(cid[:5].lower() == 'santo')

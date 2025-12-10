'''n = input('Digite seu nome: ')

if n.lower().find('silva') >=0 :
    print('Seu nome tem silva')
else:
    print('Seu nome n tem silva')'''

n = str(input('Digite seu nome: ')).strip()
print('silva' in n.lower())

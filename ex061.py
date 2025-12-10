print('Primeiros 10 termos de uma PA')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
contador = 1

while contador <= 10 :
    print(decimo_termo, end=' -> ')
    contador += 1
print('Acabou')

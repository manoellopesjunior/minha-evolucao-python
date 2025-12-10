from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}° pessoa nasceu? '))
    idade  = atual - nasc
    if idade >= 18:
       total_maior += 1
    else:
        total_menor += 1
print(f'Ao total tivemos {total_maior} pessoas maiores de idade.')
print(f'Ao total tivemos {total_menor} pessoas menores de idade.')

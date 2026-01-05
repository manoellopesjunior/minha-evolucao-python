time = []

while True:
    jogador = {}
    gol = []
    saldo = 0
    
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    
    for j in range(jogador['Partidas']):
        g = int(input(f'   Quantos Gols na partida {j+1}°? '))
        saldo += g
        gol.append(g)
    
    jogador['Total'] = saldo
    jogador['Gols'] = gol
    time.append(jogador.copy())
    
    continuar = input('Deseja Continuar? [S/N]: ').strip().upper()[0]
    print("'='-" * 13)
    while continuar not in 'SN':
        continuar = input('Erro! Digit apenas S ou N: ').strip().upper()[0]
    if continuar == 'N':
        break

print('=' * 45)
print(f'cod  nome           gols            total')
for i, jogador in enumerate(time):
        print(f'{i:<4}   {jogador["Nome"]:<14} {str(jogador["Gols"]):<15} {jogador["Total"]}')

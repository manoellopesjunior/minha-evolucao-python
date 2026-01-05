jogador = {}
jogador['Nome'] = str(input('Nome: '))
jogos = int(input(f'Quantas Partidas {jogador["Nome"]} jogou? '))
gol = []
tot = 0
for i in range(jogos):
    n = int(input(f'Quantos gols na partida {i+1}? '))
    tot += n
    gol.append(n)
jogador['Gols'] = gol
jogador['Total'] = tot
print('=-' * 35)
print(jogador)
print('=-' * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 35)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas.')
for i, c in enumerate(gol):
    print(f'   => Na partida {i+1}, fez {c} gols.')
print(f'Foi um total de {tot} Gols.')
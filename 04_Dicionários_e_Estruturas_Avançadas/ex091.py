from random import randint as r
from time import sleep
from operator import itemgetter as it
d = {}
print('== VALORES SORTEADOS ==')
for c in range(1, 5):
    d[f'Jogador{c}']= r(1, 6)
    print(f'O jogador{c}° tirou {d[f"Jogador{c}"]} no dado.')
    sleep(1)
rank = sorted(d.items(), key=it(1), reverse=True )
print('-=' * 17)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(rank):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

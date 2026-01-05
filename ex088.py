from random import sample as s
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
n = int(input('Quantos jogos voçê quer que eu sorteie? '))
print(f'{f"SORTEANDO {n} JOGOS":-^40}')
for c in range(1, n+1):  
    print(f'Jogo {c}: {s(range(1, 60), 6)}')
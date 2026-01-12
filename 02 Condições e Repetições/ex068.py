from random import randint as r
print('-=' * 20)
print('Vamos jogar PAR ou ÍMPAR!')
print('-=' * 20)
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if par_impar not in 'PI':
        print('Opção inválida! Tente novamente.')
        continue
    computador = r(0, 10)
    total = jogador + computador
    if total % 2 == 0 and par_impar == 'P':
        print(f'Você jogou {jogador} e o computador {computador}.')
        print(f'Total de {total} DEU PAR')
        vitorias += 1
        print('Você VENCEU! Vamos jogar novamente...')
    elif total % 2 != 0 and par_impar == 'I':
        print(f'Você jogou {jogador} e o computador {computador}.')
        print(f'Total de {total} DEU ÍMPAR')
        print('Você VENCEU! Vamos jogar novamente...')
        vitorias += 1
    else:
        print(f'Você jogou {jogador} e o computador {computador}.')
        print(f'Total de {total} DEU {"PAR" if total % 2 == 0 else "ÍMPAR"}')
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {vitorias} vezes.')

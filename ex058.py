'''from random import randint
numero = 0
n = -1
while n != 0:
    pensar = randint(0, 10)
    n = int(input('Tente acertar o número do computardor entre (0, 10): '))
    print(f'O numero escolhido foi {pensar} e vc digitou o numero {n}')
    numero += 1
    if n == pensar:
        print('Acertou')
        break
    else:
        print('Errou! vou pensar outro numero.')
print(f'Você tentou {numero} vezes até acertar')'''

from random import randint
pensar = randint(0, 10)
print('Vou pensar em um número, tente acertar!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpites += 1
    if jogador == pensar:
        acertou = True
    else:
        if jogador < pensar:
            print('Mais... Tente novamente.')
        elif jogador > pensar:
            print('Menos... Tente novamente.')
print(f'Acertou com {palpites} tentativas')

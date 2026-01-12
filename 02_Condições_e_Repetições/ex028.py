from random import randint

print('Bom dia!!! Vamos jogar.')
print('Sortearei um numero de 0 a 5, tente acertar')
n = int(input('Digite um numero: '))   # jogador insere um numero
b = randint(0,5)                 # maquina insere um numero

if b == n:                             # if :  compara os dois numeros
    print('Parabens você acertou!')   # se jogador for igual maquina acertou
else:
    print('Você errou , meu numero era {}'.format(b))  # se não maquina ganhou
print('Fim do jogo!')

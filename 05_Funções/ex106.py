c = ('\033[m',        #0 sem cor
     '\033[0;30;41m', #1 vermelho
     '\033[0;30;42m', #2 verde
     '\033[0;30;44m', #3 azul
     '\033[7;30m'     #4 branco
)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

def ajuda(com):
    titulo(f'acessando o manual do comando \"{com}\"',4)
    print(c[4], end='')
    help(com)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
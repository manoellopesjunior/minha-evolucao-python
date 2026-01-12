#função
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

# programa principal
escreva('Gustavo Guanabara')
escreva('Curso Python no Youtube')
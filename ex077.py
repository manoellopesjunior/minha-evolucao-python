lista = ('computador', 'teclado', 'monitor', 'mouse', 'internet', 'software', 'hardware', 'programa',
'codigo', 'servidor', 'banco', 'dados', 'sistema', 'aplicaçao', 'usuario')
vogais = 'aeiou'
for palavra in lista:
    print(f'Na palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()




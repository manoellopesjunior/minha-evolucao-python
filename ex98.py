from time import sleep 
# o uso do flush=true, é pq o sleep() está dando bug de tela

def cont1(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        c = i
        while c <=f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c += p
        print('Fim!')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c -= p
        print('Fim!')

def l():
    l = print('-' * 35)


l()
cont1(1, 10, 1)
l()
cont1(10, 0, 2)
l()
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim:    '))
c = int(input('Passo:  '))
cont1(a, b, c)
l()

def fatorial(n, show=False):
    """
    -> calcula o fatorial do número: seria um numero vezes o seu antecessor : 'n' * 'n-1' 
    Parametro show = O uso do show é para mostrar a conta completa ou só o resultado final.
    Parametro n = O numero a ser calculado
    Parametro return = retorna o valor final do fatorial de n
    """
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)
    

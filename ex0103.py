def ficha(n="", g="0"):
    """
    Descrição de ficha()

    :param n: recolhe o nome
    :param g: recolhe os gols
    :g.isdigit: confirmo se g de fora é um numero inteiro, se for o g de detro recebe esse valor
    se n for o resultado final é '0'
    n.strip: elimina os espaços vazio, se tiver vazio 'n' recebe desconhecido , se não, não faz nada pq o 'return' 
    retorna o nome de fora da função
    """
    #trata gols
    if g.isdigit():
        g = int(g)
    else:
        g = 0
    #trata nome
    if n.strip() == "":
        n = "<desconhecido>"

    return f'O jogador {n} fez {g} gol(s) no campeonato'    
    
    

print('-' * 30)    
n = input('Nome do Jogador: ')
g = input('Número de Gols: ')
print('-' * 30) 
print(ficha(n, g))
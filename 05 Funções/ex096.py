#função
def area(l, c):
    t = l * c
    print(f'A área de um terreno {l}m² x {c}m² é de {t:.1f}m²')
#função do titulo
def l(txt):
    l = print('-' * 20)
    print(txt)
    l = print('-' * 20)
#programa Principal
l("Controle de Terrenos")
l = float(input('Largura (m²): '))
c = float(input('Comprimento (m²): '))
area(l, c)

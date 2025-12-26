lista = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <=20:
        print(f'Voçê Digitou {lista[n]}')
        continuar = input('Voçê desenja continuar [S/N]: ').strip().upper()[0]
        if continuar == 'S':
            continue
        else:
            break
    if n <= 0 or n >=20:
        print('Tente novamente.', end= ' ')


print('Fim do Programa!!!')


print('=' * 30)
print('Caixa Eletrônico')
print('=' * 30)
qtd_50 = qtd_20 = qtd_10 = qtd_1 = 0
#pedir um valor até ele ser valido
while True:
    try:
        sacar = int(input('Qual valor você quer sacar? R$ '))
        if sacar > 0:
            break
        else:
            print('Por favor, digite um valor positivo.')
    except ValueError:
        print('Valor inválido. Por favor, digite um número inteiro.')
#calcular a quantidade de cada cédula
while sacar > 0:
    if sacar >= 50:
        sacar -= 50
        qtd_50 += 1 
    elif sacar >= 20:
        sacar -= 20
        qtd_20 += 1

    elif sacar >= 10:
        sacar -= 10
        qtd_10 += 1 
    else:
        sacar -= 1
        qtd_1 += 1
#mostrar o resultado
print('Você receberá:')
if qtd_50 > 0:
    print(f'Total de {qtd_50} cédulas de R$50')
if qtd_20 > 0:
    print(f'Total de {qtd_20} cédulas de R$20')
if qtd_10 > 0:
    print(f'Total de {qtd_10} cédulas de R$10')
if qtd_1 > 0:
    print(f'Total de {qtd_1} cédulas de R$1')
print('Obrigado por usar nosso caixa eletrônico!')




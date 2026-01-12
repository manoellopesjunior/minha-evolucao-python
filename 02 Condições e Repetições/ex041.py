nasc = int(input('Digite o seu ano de nascimento: '))
idade = 2025 - nasc
if idade <= 9:
    print(f'Voce tem {idade} anos.')
    print('Sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Voce tem {idade} anos.')
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Voce tem {idade} anos.')
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print(f'Voce tem {idade} anos.')
    print('Sua categoria é SÊNIOR')
else:
    print(f'Voce tem {idade} anos.')
    print('Sua categoria é MASTER')

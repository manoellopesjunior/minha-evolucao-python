'''data = int(input('Em que ano você nasceu? '))
idade = 2025 - data
passou = idade - 18
faltou = 18 - idade

if idade < 18:
    print(f'Você tem {idade} anos')
    print(f'Você é menor idade , falta {faltou} anos para se alistar.')

elif idade ==18:
    print(f'Você tem {idade} anos')
    print('Está na hora de se alistar')
else:
    print(f'Voce tem {idade} anos')
    print(f'Vecê esta com o alistamento atrasado há {passou} anos, aliste-se imediatamente. ')'''

from datetime import date
atual = date.today().year
sexo = str(input('Digite seu sexo (M/F): ')).upper()
if sexo == 'M':
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print(f'Quam nasceu em {nasc} tem {idade} anos em {atual}')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Você ainda não tem 18 anos. Ainda falta {saldo} anos para o alistamento')
        ano = atual = saldo
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você já deveria ter se alistado há {saldo} anos')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano} anos')
else:
    print('Você não precisa fazer alistamento militar obrigatório')


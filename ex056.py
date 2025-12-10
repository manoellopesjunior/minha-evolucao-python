soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulher_menos_20 = 0

for pessoa in range(1,5):
    print(f'---- {pessoa}° PESSOA ---')
    nome = str(input('nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20 += 1

media_idade = soma_idade / 4
print(f'\nA média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho} ')
print(f'Ao todo são {mulher_menos_20} mulheres com menos de 20 anos.')

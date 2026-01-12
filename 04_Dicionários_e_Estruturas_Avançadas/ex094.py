'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pasta = []
pessoa = {}
tot_pessoa = 0
media = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    tot_pessoa += 1
    sexo = input('Sexo: [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('ERRO! Por favor, digite apenas M ou F: ').strip().upper()[0]
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Idade: '))
    media += pessoa['Idade']
    pasta.append(pessoa.copy())

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Erro! Digit apenas S ou N: ').strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 35)
print(f'Ao todo temos {tot_pessoa} pessoas cadastradas.')

media = media / tot_pessoa
print(f'A média de idade é de {media:.2f}')

print(f'As mulheres cadastradas foram: ', end=' ')
for pessoa in pasta:
    if pessoa['Sexo'] == 'F':
        print(f'{pessoa["Nome"]}', end=' ')
print()

print('Lista das pessoas que estão acima da média:')
for pessoa in pasta:
    if pessoa['Idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}', end=' ')
        print()

print('<< ENCERRADO >>')



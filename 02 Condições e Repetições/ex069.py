
maiores = 0
homens = 0
mulheres_menores = 0

while True:
    print('-' * 20)

    # validar idade das pessoas
    while True:
        idade = input("Digite a idade da pessoa: ")
        if idade.isdigit():
            idade = int(idade)
            break
        print("Idade inválida! Digite apenas números.")

    # validar sexo das pessoas
    sexo = input("Digite o sexo da pessoa [M/F]: ").strip().upper()[0]
    while sexo not in 'MF':
        sexo = input("Sexo inválido! Digite [M/F]: ").strip().upper()[0]

    # contadores
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores += 1

    # continuar
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()[0]
    while continuar not in 'SN':
        continuar = input("Opção inválida! [S/N]: ").strip().upper()[0]

    if continuar == 'N':
        break

print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menores}')





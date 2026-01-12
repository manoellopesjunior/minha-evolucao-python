#lista principal
lista = []
#laço para inserir aluno e notas na lista secundaria alunos
while True:
    alunos = []
    #inserção de dados
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    # adicionar dados a lista secundaria
    alunos.append(nome)
    alunos.append(nota1)
    alunos.append(nota2)
    # adicionar lista secundaria a principal
    lista.append(alunos)
    #laço para continuar ou não
    continuar = input('Quer continuar [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Quer continuar ? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<15}{"Média":>8}')
print('-' * 40)

# Percorre a lista usando índice
for i in range(len(lista)):
    nome = lista[i][0]
    media = (lista[i][1] + lista[i][2]) / 2
    print(f'{i:<4}{nome:<15}{media:>8.1f}')

print('-' * 40)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    # Condição de saída
    if opcao == 999:
        print('Finalizando...')
        break

    # Verifica se o índice existe
    if opcao < len(lista):
        print(f'Notas de {lista[opcao][0]} são '
              f'{lista[opcao][1]} e {lista[opcao][2]}')
    else:
        print('Aluno não encontrado!')

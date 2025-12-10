print('Insira as duas notas do aluno abaixo.')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'A média do aluno é {media}. Aluno Reprovado.')
elif media >= 5.0 and media < 7:
    print(f'A media do aluno é {media}. Aluno de Recuperação.')
else:
    print(f'A media do aluno é {media}. Aluno Aprovado.')

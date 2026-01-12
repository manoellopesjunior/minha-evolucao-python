dic = {}

dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Média de {dic["nome"]} :'))
if dic['media'] >= 7.0:
    dic['situação'] = 'Aprovado'
elif 5 <= dic['media'] < 7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
print('-=' * 20)
for k, v in dic.items():
    print(f' - {k} é igual a {v}')

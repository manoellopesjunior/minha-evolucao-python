from datetime import datetime as data
dic = {}
dic['Nome'] = str(input('Nome: '))
dic['Idade'] = data.now().year - int(input('Ano de Nascimento: '))
dic['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if dic['CTPS'] != 0:
    dic['Contratação'] = int(input('Ano de Contratação: '))
    dic['Salário'] = float(input('Salário: R$'))
    dic['Aposentadoria'] = dic['Idade'] + ((dic['Contratação'] + 35) - data.now().year) 
    
print('=-' * 30 )
for k, v in dic.items():
    print(f'- {k} tem o valor: {v}')
n = str(input('Digite um nome completo: ')).strip()   #strip é para remover os espaços desnecessarios

nomes =  n.split()

print('Seu primeiro nome é :{}'.format(nomes[0])) #zero é sempre o primeiro nome ou primeira letra
print('Seu ultimo nome é :{}'.format(nomes[-1])) # o uso do -1 é para achar a ultima palavra ou nome ou letra

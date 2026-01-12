f = str(input('Digite um frase: ')).strip()
a = f.lower().count('a')
b = f.find('a') + 1
c = f.rfind('a') + 1

print()
print('A letra (A) aparece {} vezes'.format(a))
print('A primeira letra (A) aparece no lugar da {}° letra'.format(b))
print('A ultima letra (A) aparece no lugar da {}° letra'.format(c))

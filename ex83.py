
n = input('Digite uma expressão matemática qualquer, que use parênteses(): ')
cont = 0
erro = False
for item in n:
    if item == '(':
        cont += 1
    if item == ')':
        cont -= 1
    if cont < 0 :
        erro = True
        break

if not erro and cont == 0:
    print('Sua expressão é valida.')
else:
    print('Sua expressão está errada.')

'''n = str(input('Digite uma expressão: ))
pilha = []
for item in n:
    if item == '(':
        pilha.append('(')
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break 
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')'''


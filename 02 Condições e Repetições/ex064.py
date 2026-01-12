n = int(input('Digite um número [999 para parar]: '))
contador = 0
soma = 0
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Voçê digitou {contador} números e a soma entre eles foi {soma}')

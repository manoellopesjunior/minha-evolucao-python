contador = soma = 0
while True:
    n = int(input("Digite um número inteiro positivo (999 para parar): "))
    if n == 999:
        break
    soma += n
    contador += 1
print(f"A soma dos {contador} números digitados é {soma}.")

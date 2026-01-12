mais = 0
total = 0
menor_preco = None
nome_barato = ""
while True:
    nome = input("Nome do produto: ")
    while True:
        try:
            preco = float(input("Preço: R$ "))
            if preco < 0:
                print("Preço inválido! Digite um valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido para o preço.")
    
    if preco > 1000:
        mais += 1
    total = total + preco
    if menor_preco is None or preco < menor_preco:
        menor_preco = preco
        nome_barato = nome
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in 'SN':
        continuar = input("Opção inválida! [S/N]: ").strip().upper()[0]

    if continuar == 'N':
        break

print(f"O total gasto na compra foi R$ {total:.2f}")
print(f"Temos {mais} produtos custando mais de R$ 1000.00")
print(f"O produto mais barato foi {nome_barato} que custa R$ {menor_preco:.2f}") 

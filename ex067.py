n = 0
while True:
    print('-' * 20)
    n = int(input("Quer a tabuada de qual valor? (0 para parar) "))
    print('-' * 20)
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
        
print("Programa de tabuada encerrado. Volte sempre!")
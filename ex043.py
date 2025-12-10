p = float(input('Qual o seu peso: '))
a = float(input('QUal a sua altura: '))
imc = p / (a ** 2)

if imc < 18.5:
    print(f'Seu imc é de: {imc:.2f}, vc está abaixo do peso.')
elif imc >=18.5 and imc < 25:
    print(f'Seu imc é de: {imc:.2f}, vc esta no peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu imc é de: {imc:.2f}, vc esta com sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'Seu imc é de: {imc:.2f}, vc esta com obesidade.')
else:
    print(f'Seu imc é de: {imc:.2f}, vc esta com obesidade mórbida.')
    print('Procure um médico urgentemente.')

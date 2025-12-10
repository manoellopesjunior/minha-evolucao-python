print('='*40)
print('Caixa'.center(40))
print('='*40)
print(''' FORMAS DE PAGAMENTO
[ 1 ]  À vista dinheriro/cheque 10% desconto.
[ 2 ]  À vista no cartão 5% desconto
[ 3 ]  Até 2x no cartão valor normal
[ 4 ]  3x ou mais no cartão 20% de juros''')
print('='*40)
v = float(input('Qual o valor do produto? R$ '))
opcao = int(input('Escolha a opção de pagamento (1-4): '))
print('='*40)
if opcao == 1:
    total = v - (v * 0.10)
    print(f'Pagamento à vista em dinheiro/cheque com\n10% de desconto.')
elif opcao == 2:
    total = v - (v * 0.05)
    print(f'Pagamento à vista no cartão com 5% de desconto.')
elif opcao == 3:
    total = v
    parcela = total / 2
    print(f'Pagamento em até 2x no cartão (sem juros).')
elif opcao == 4:
    total = v + (v * 0.20)
    total_parcela = int(input('Quantas parcelas? '))
    parcela = total / total_parcela
    print(f'Pagamento em 3x ou mais no cartão com 20% de juros.')
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(total_parcela, parcela))
else:
    total = v
    print('Opção inválida de pagamento, tente novamente!')
if total is not None:
    print(f'\nValor final: R$ {total:.2f}')
print('='*40)

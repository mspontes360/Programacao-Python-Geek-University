"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# o total a pagar com desconto de 10%;
# o valor de cada parcela, no parcelamento de 3x sem juros;
# a comissão do vendedor, no caso de venda ser a vista(5% sobre o valor com desconto);
# a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

total_amount = float(input("Enter the total amount: "))
in_cash = total_amount - total_amount * 0.10
portion = total_amount / 3
commission_in_cash = in_cash * 0.05
commission_portion = total_amount * 0.05

print(f'Total amount payable at a discount: {in_cash}')
print(f'Value of each portion: {portion}')
print(f'Commission in cash {commission_in_cash}')
print(f'Installment sale commission {commission_portion}')



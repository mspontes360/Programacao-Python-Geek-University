"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá
ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

VENDA MENSAL                                                    COMISSÃO
Maior ou igual a R$100.000,00                           R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00   R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00    R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00    R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00    R$500,00 + 14% das vendas
Menor que R$20.000,00                                   R$400,00 + 14% das vendas
"""

sale_amount = float(input("Enter the sale amount: "))

if sale_amount >= 100000.00:
    comission = 700.00 + sale_amount * 0.16
elif sale_amount < 100000.00 and sale_amount >= 80000.00:
    comission = 650.00 + sale_amount * 0.14
elif sale_amount < 80000.00 and sale_amount >= 60000.00:
    comission = 600.00 + sale_amount * 0.14
elif sale_amount < 60000.00 and sale_amount >= 40000.00:
    comission = 550.00 + sale_amount * 0.14
elif sale_amount < 40000.00 and sale_amount >= 20000.00:
    comission = 500.00 + sale_amount * 0.14
else:
    comission = 400.00 + sale_amount * 0.14

print(comission)
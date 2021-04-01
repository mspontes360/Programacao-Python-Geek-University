"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete
e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da
lanchonete segue o padrão abaixo:

ESPECIFICAÇÃO           CÓDIGO      PREÇO
Cachorro Quente         100         1.20
Bauru Simples           101         1.30
Bauru com ovo           102         1.50
Hamburguer              103         1.20
Cheeseburguer           104         1.70
Suco                    105         2.20
Refrigerante            106         1.00
"""

code = int(input("Enter the code: "))
quantity = float(input("Enter the quantity: "))

if code == 100:
    value = quantity * 1.20
elif code == 101:
    value = quantity * 1.30
elif code == 102:
    value = quantity * 1.50
elif code == 103:
    value = quantity * 1.20
elif code == 104:
    value = quantity * 1.70
elif code == 105:
    value = quantity * 2.20
else:
    value = quantity * 1.00

print(f'The amount payable is: {value}.')

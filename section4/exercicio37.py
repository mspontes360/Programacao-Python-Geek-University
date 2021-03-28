"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto,
tendo em vista que o desconto foi de 12%.
"""

value = float(input("Enter the value of the product: "))

discount = value - value * 0.12

print(f'The value of the discounted product is {discount}.')

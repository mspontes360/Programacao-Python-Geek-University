"""
Faça um programa para ler as dimensões de um terreno (comprimento 'c' e largura 'l'),
bem como o preço do metro de tela 'p'. Imprima o custo para cercar este mesmo
terreno com tela
"""

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
screen_price = float(input("Enter the screen price: "))

length_total = length * 2  + width * 2

total = length_total * screen_price

print(f'The cost for fence the terrain is {total}.')

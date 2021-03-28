"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados.
A fórmula de conversão é M = H * 10000, sendo M  área em metros quadrados
e A a área em acres.
"""

hectares = float(input("Enter an area value in hectares: "))

square_meters = hectares * 10000

print(f'The area is square meters is: {square_meters}')
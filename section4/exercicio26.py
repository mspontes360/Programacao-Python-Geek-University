"""
Leia um valor de área em metros quadrados e apresente-o convertido em hectares.
A fórmula de conversão é H = M * 0.0001, sendo M  área em metros quadrados
e H a área em hectares.
"""

square_meters = float(input("Enter an area value in square meters: "))

hectares = square_meters * 0.0001

print(f'The area in hectares is: {hectares}')
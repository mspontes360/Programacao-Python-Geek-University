"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados.
A fórmula de conversão é M = A * 4048.58, sendo M  área em metros quadrados
e A a área em acres.
"""

acre = float(input("Enter an area value in acres: "))

square_meters = acre * 4048.58

print(f'The area is square meters is: {square_meters}')
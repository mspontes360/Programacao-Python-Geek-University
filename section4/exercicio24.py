"""
Leia um valor de área em metros quadrados e apresente-o convertido em acres.
A fórmula de conversão é A = M * 0.000247, sendo M  área em metros quadrados
e A a área em acres.
"""

square_meters = float(input("Enter an area value in square meters: "))

acre = square_meters * 0.000247

print(f'The acreage is: {acre}')
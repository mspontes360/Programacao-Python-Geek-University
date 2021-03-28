"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A fórmula de conversão é J = M / 0.91, sendo J o comprimento em jardas e M
o comprimento em metros.
"""

meters = float(input("Enter a length value is meters: "))

yards = meters / 0.91

print(f'The length in yards is: {yards}')
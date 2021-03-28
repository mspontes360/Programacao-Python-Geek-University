"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A fórmula de conversão é M = 0.91 * J, sendo J o comprimento em jardas e M
o comprimento em metros.
"""

yards = float(input("Enter a length value is yards: "))

meters = 0.91 * yards

print(f'The length in meters is: {meters}')
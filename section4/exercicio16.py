"""
Leia um valor de comprimento em polegadas e apresente-o convertido em
centímetros. A fórmula de conversão é C = P * 2.54, sendo C o comprimento em
centímetros e P o comprimento em polegadas.
"""

inches = float(input("Enter a length in inches: "))

centimeters = inches * 2.54

print(f'The length in centimeter is {centimeters}')

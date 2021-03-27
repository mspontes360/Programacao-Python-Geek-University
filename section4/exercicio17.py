"""
Leia um valor de comprimento em centimetros e apresente-o convertido em
polegadas. A fórmula de conversão é P = C / 2.54, sendo C o comprimento em
centímetros e P o comprimento em polegadas.
"""

centimeters = float(input("Enter a length in centimeters: "))

inches = centimeters / 2.54

print(f'The length in inches is {inches}')

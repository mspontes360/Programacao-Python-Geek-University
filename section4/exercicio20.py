"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é L = K / 0.45, sendo K a massa em quilogramas e L
a massa em libras.
"""

kilograms = float(input("Enter a mass value in kilograms: "))

pounds = kilograms / 0.45

print(f'The mass in pounds is: {pounds}')
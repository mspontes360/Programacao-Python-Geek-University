"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é K = L * 0.45, sendo K a massa em quilogramas e L
a massa em libras.
"""

pounds = float(input("Enter a mass value in pounds: "))

kilograms = pounds * 0.45

print(f'The mass in kilograms is: {kilograms}')
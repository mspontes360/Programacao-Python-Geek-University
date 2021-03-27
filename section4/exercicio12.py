"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A
fórmula de conversão é K = 1.61 * M, sendo K a distância em quilômetro e
M em milhas.
"""

miles = float(input("Enter distance in miles: "))

kilometers = 1.61 * miles

print(f'The distance in kilometers is: {kilometers}')

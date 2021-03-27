"""
Leia uma distância em quilômetros e apresente-a convertida em milhas. A
fórmula de conversão é M = K / 1.61, sendo K a distância em quilômetro e
M em milhas.
"""

kilometers = float(input("Enter distance in kilometers: "))

miles = kilometers / 1.61

print(f'The distance in miles is: {miles}')

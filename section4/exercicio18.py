"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é L = 1000 * M, sendo L o volume em litros e M o volume
em metros cúbicos.
"""

meters = float(input("Enter a volume value in cubic meters: "))

liters = 1000 * meters

print(f'The volume in liters is: {liters}')
"""
Leia um valor de volume em litros e apresente-o convertido em litros metros cúbicos.
A fórmula de conversão é M = L / 1000, sendo L o volume em litros e M o volume
em metros cúbicos.
"""

liters = float(input("Enter a volume value in cubic meters: "))

meters = liters / 1000

print(f'The volume in liters is: {meters}')
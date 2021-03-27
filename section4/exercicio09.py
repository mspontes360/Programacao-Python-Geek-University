"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é K = C + 273.15, sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""

tempCelsius = float(input("Enter the temperature in Celsius: "))

tempKelvin = tempCelsius + 273.15

print(f'The temperature in Kelvin is {tempKelvin}º')

"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é C = K - 273.15, sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""

tempKelvin = float(input("Enter the temperature in Celsius: "))

tempCelsius = tempKelvin - 273.15

print(f'The temperature in Celsius is {tempCelsius}º')

"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é K = C + 273.15, sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""

temp_Celsius = float(input("Enter the temperature in Celsius: "))

temp_Kelvin = temp_Celsius + 273.15

print(f'The temperature in Kelvin is {temp_Kelvin}º')

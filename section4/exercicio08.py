"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é C = K - 273.15, sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""

temp_Kelvin = float(input("Enter the temperature in Celsius: "))

temp_Celsius = temp_Kelvin - 273.15

print(f'The temperature in Celsius is {temp_Celsius}º')

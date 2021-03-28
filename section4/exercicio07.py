"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""

temp_Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

temp_Celsius = 5.0 * (temp_Fahrenheit - 32.0) / 9.0

print(f'The temperature in Celsius is {temp_Celsius}º')

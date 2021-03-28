"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

temp_Celsius = float(input("Enter the temperature in Celsius: "))

temp_Fahrenheit = temp_Celsius * (9.0 / 5.0) + 32.0

print(f'The temperature in Fahrenheit is {temp_Fahrenheit}º')

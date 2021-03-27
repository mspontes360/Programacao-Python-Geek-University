"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é F = C * (9.0 / 5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""

tempCelsius = float(input("Enter the temperature in Celsius: "))

tempFahrenheit = tempCelsius * (9.0 / 5.0) + 32.0

print(f'The temperature in Fahrenheit is {tempFahrenheit}º')

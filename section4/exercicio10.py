"""
Leia  uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K / 3.6, sendo K a velocidade em
km/h e M em m/s.
"""

kilometers_Per_Hour = float(input("Enter a speed in kilometers per hour: "))

meters_Per_Second = kilometers_Per_Hour / 3.6

print(f'The speed in meters per second is {meters_Per_Second}')

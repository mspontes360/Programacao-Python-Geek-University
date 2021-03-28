"""
Leia  uma velocidade em m/s (metros por segundo) e apresente-a convertida
em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K
a velocidade em km/h e M em m/s.
"""

meters_Per_Second = float(input("Enter a speed in meters per second: "))

kilometers_Per_Hour = meters_Per_Second * 3.6

print(f'The speed in kilometers per hour is {kilometers_Per_Hour}')

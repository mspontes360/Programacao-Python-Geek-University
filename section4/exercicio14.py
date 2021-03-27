"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de
conversão é R = G * pi / 180, sendo G o ângulo em graus e R em radianos
e pi = 3.14.
"""

degrees = float(input("Enter an angle in degrees: "))

pi = 3.14

radians = degrees * pi / 180

print(f'The angle in radians is: {radians}')

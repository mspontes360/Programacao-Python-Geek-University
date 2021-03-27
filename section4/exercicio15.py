"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de
conversão é G = R * 180 / pi, sendo G o ângulo em graus e R em radianos
e pi = 3.14.
"""

radians = float(input("Enter an angle in radians: "))

pi = 3.1415

degrees = radians * 180 / pi

print(f'The angle in degrees is: {degrees}')

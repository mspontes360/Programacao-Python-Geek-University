"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O
volume de um cilindro é calculado por meio da seguinte fórmula:
V = pi * raio² * altura, onde pi é 3.141592.
"""

height = float(input("Enter the height of the cylinder: "))
radius = float(input("Insert the radius of the cylinder: "))
pi = 3.141592

volume = pi * (radius * radius) * height

print(f'The volume of the cylinder is {volume}.')

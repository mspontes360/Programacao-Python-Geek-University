"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma
das seguintes médias de acordo com um valor numérico digitado pelo usuário:

a) Geométrica:
    ³V x * y * 2

b) Ponderada:
    (x + 2 * y + 3 * z) / 6

c) Harmônica:
    1 / ((1/x) + (1/y) + (1/z))

d) Aritmética:
    (x + y + z) / 3
"""

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
z = int(input("Enter the value of z: "))


geometric = (x * y * 2) ** (1/3)

weighted = (x + 2 * y + 3 * z) / 6

harmonic = 1 / ((1/x) + (1/y) + (1/z))

arithmetic = (x + y + z) / 3

print(f'Geometric = {geometric}')
print(f'Weighted = {weighted}')
print(f'Harmonic = {harmonic}')
print(f'Arithmetic = {arithmetic}')

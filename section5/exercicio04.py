"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# O número digitado ao quadrado
# A raiz quadrada do número digitado
"""

number = float(input("Enter a real number: "))

if number > 0:
    number_squared = number * number
    square_root = number ** 0.5

print(f'The number squared is {number_squared} and the square root of the number is {square_root}')
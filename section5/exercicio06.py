"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    print(f'The first number {number1} is greater than the second number {number2}')
    print(f'The difference between them is {number1 - number2}')
else:
    print(f'The second number {number2} is greater than the first number {number1}')
    print(f'The difference between them is {number2 - number1}')

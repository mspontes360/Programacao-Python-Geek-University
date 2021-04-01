"""
Faça um programa que receba um número inteiro e verifique se ele é par ou ímpar.
"""

number = float(input('Enter the number: '))

if number % 2 == 0:
    print(f'The number {number} is pair')
else:
    print(f'The number {number} is odd')


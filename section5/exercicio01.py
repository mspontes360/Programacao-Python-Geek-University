"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

if number1 > number2:
    print(f'The largest number you entered was: {number1}')
elif number1 == number2:
    print(f'You typed two identical numbers: {number1}')
else:
    print(f'The largest number you entered was: {number2}')

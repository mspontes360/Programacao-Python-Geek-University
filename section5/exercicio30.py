"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 < number2 < number3:
    print(f'{number1}{number2}{number3}')
elif number1 < number3 < number2:
    print(f'{number1}{number3}{number2}')
elif number2 < number1 < number3:
    print(f'{number2}{number1}{number3}')
elif number2 < number3 < number1:
    print(f'{number2}{number3}{number1}')
elif number3 < number1 < number2:
    print(f'{number3}{number1}{number2}')
else:
    print(f'{number3}{number2}{number1}')


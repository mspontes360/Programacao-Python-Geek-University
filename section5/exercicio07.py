"""
Faça um programa que receba dois números e mostre o maior. Se por acaso os dois
números forem iguais, imprima a mensagem 'Números iguais'.
"""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    print(f'The first number {number1} is greater than the second number {number2}')
elif number2 > number1:
    print(f'The second number {number2} is greater than the first number {number1}')
else:
    print("Equal numbers.")
"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas
(as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então
pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""

print("Calculator")
print("Choose the option: \n1- addition. \n2- subtraction.")
print("3- multiplication. \n4- division.")

option = int(input("Option: "))

if option == 1:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    addition = number1 + number2
    print(addition)
elif option == 2:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    subtraction = number1 - number2
    print(subtraction)
elif option == 3:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    multiplication = number1 * number2
    print(multiplication)
elif option == 4:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    division = number1 / number2
    print(division)
else:
    print('Invalid operation')


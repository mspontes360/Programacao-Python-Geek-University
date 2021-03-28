"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados
dos três valores lidos.
"""

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

square_numbers = (first_number * first_number) + (second_number * second_number) + (third_number * third_number)

print(f'The sum of the squres of the numbers is: {square_numbers}')

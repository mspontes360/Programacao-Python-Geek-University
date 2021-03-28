"""
Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""

first_note = float(input("Insert the first note: "))
second_note = float(input("Insert the second note: "))
third_note = float(input("Insert the third note: "))

arithmetic_average = first_note + second_note + third_note / 3

print(f'The arithmetic average is {arithmetic_average}')
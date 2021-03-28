"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo
que ele recebeu um aumento de 25%.
"""

salary = float(input("Enter the salary amount: "))

new_salary = salary + salary * 0.25

print(f'The new salary amount is {new_salary}.')
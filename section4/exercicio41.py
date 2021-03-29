"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""

work_value = float(input("Enter the hourly work value: "))
hours_worked = float(input("Enter the number of hours worked: "))
value_worked = work_value * hours_worked
calculated_value = value_worked * 0.10 + value_worked

print(f'The amount to be paid is {calculated_value}')

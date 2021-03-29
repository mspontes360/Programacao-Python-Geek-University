"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""

base_salary = float(input("Enter the base salary: "))
bonus = 0.05
tax = 0.07

base_salary_bonus = base_salary * bonus
base_salary_tax = base_salary * tax
salary_receivable = base_salary + base_salary_bonus - base_salary_tax

print(f'The salary receivable is {salary_receivable}')

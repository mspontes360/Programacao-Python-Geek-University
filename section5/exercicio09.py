"""
Leia o salário de um trabalhador e o valor da prestação de um emprétismo.
Se a prestação for maior  que 20% do salário imprima: "Empréstimo não concedido",
caso contrário imprima: "Empréstimo condedido".
"""

salary = float(input('Enter your salary: '))
parcel = float(input('Enter the parcel value: '))

if parcel > salary * (20/100):
    print(f'Loan not granted')
else:
    print(f'Loan granted')

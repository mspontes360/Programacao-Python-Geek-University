"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de 
sua idade e do ano atual.
"""

age = int(input("Enter your age: "))
year = int(input("Enter the current year: "))

birth_year = year - age

print(f'The year of birth is {birth_year}.')

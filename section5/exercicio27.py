"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:

Categoria           Idade
Infantil A          5 a 7
Infantil B          8 a 10
Juvenil A           11 a 13
Juvenil B           14 a 17
Senior              maiores de 18 anos

"""

age = int(input("Enter the age: "))

if age >= 5 and age <=7:
    print("Childish A")
elif age >= 8 and age <= 10:
    print("Childish B")
elif age >= 11 and age <= 13:
    print("Juvenile A")
elif age >= 14 and age <= 17:
    print("Juvenile B")
else:
    print("Senior")

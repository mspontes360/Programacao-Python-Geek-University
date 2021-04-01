"""
Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro
em um percurso calcule o consumo em km/l e escreva uma mensagem de acordo com a
tabela abaixo:

CONSUMO     (km/l)      MENSAGEM
menor que     8         Venda o carro!
entre       8 e 14      Econômico!
maior que     14        Super econômico!
"""

distance = float(input("Enter the disctance: "))
liters = float(input("Enter the number os liters: "))

consumption = distance / liters

if consumption < 8:
    print("Sell the car!")
elif consumption >= 8 and consumption <= 14:
    print("Economic!")
else:
    print("Super economic!")


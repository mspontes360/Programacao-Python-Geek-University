"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste número.
"""
import math

number = int(input("Enter an integer: "))

if number < 0:
    print("Invalid number")
else:
    math.log(number)


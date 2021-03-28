"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o
antecessor de seu dobro.
"""

number = int(input("Enter an integer: "))

successor = number * 3 + 1

predecessor = number * 2 - 1

print(successor + predecessor)

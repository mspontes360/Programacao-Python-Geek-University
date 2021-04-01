"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""

number = float(input("Enter a real number: "))

if number > 0:
    number = number ** 0.5
elif number == 0:
    number = 1
else:
    number = number * number

print(number)

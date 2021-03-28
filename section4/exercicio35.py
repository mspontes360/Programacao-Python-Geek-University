"""
Sejam 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é ontida pela equação:
hipotenusa = raiz quadrada de a² + b². Faça um programa que receba os valores de 'a' e
'b' e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa
operação.
"""

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

hypotenuse = ((a * a + b * b) ** 0.5)

print(f'The value of hypotenuse is {hypotenuse}')

"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um
triângulo e, se é um triângulo escaleno, equilátero ou isóscele, considerando os
seguintes conceitos:
    # O comprimento de cada lado de um triângulo é menor do que a soma dos outros
      dois lados.
    # Chama-se equilátero o triângulo que tem três lados iguais.
    # Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    # Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

"""

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))

if (a < b + c) or (b < a + c) or (c < a + b):
    if a == b == c:
        print("equilateral triangle")
    elif (a == b) or (a == c) or (c == b):
        print("isosceles triangle")
    else:
        print("scalene triangle")
    

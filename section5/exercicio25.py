"""
Calcule as raízes da equação de 2º grau.
Lembrando que:

x= -b +- raiz de delta / 2a

Onde:
delta = b² - 4ac

E ax² + bx + c = 0 representa uma equação de 2º grau.

A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem
"Não é equação de segundo grau".

* Se delta < 0, não existe raiz real. Imprima a mensagem "Não existe raiz"
* Se delta = 0, existe uma raiz real. Imprime a raiz e a mensagem "Raiz única"
* Se delta >= 0, imprima as duas raízes reais.
"""

a = float(input('Insert the variable a: '))
b = float(input('Insert the variable b: '))
c = float(input('Insert the variable c: '))

if a == 0:
    print("It's not a second degree equation")
else:
    delta = (b**2) - (4 * a * c)
    print(f'The delta value is {delta}')

    if delta < 0:
        print("There is no root")
    elif delta == 0:
        print("Single root")
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        print(f'The positive root is {x1}')

        x2 =(-b - (delta ** 0.5)) / (2 * a)
        print(f'The negative root is {x2}')


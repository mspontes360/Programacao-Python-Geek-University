"""
Leia um número fornecido pelo usuário, se esse número for positivo,calcule a raiz quadrada
do número. Se o número for negativo, mostre uma mensagem dizendo o número é inválido.
"""

number = float(input('Enter the number: '))

if number > 0:
    square = number ** 0.5
    print(f'The square root of the number entered is: {square}')
else:
    print(f'Invalid number')

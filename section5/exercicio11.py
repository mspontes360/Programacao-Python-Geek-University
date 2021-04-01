"""
Escreva um prigrama que leia um número inteiro maior do que zero e devolva na tela a soma
dde todos os seus algarismos. Por exemplo, número 251 corresponderá a 8 (2 + 5 + 1). Se o
número lido não for maior do que zero, o programa terminará com a mensagem: "Número inválido".
"""

numero = input('Enter a number greater than zero: ')

if int(numero) < 0:
    print("Invalid number!")
else:
    print(sum(int(i) for i in numero))

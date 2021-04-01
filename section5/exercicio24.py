"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa
em que o usuário entre com o valor e o estado destino do produto e o programa retorne o
preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado
digitado não for válido, mostrar uma mensagem de erro.
"""

print('Tax calculator')
valor = float(input('Hello. Please enter the product value: '))

print('Choose the destination state of the product:')
print('1- MG \n2- SP \n3- RJ \n4- MS')
estado = float(input('State: ' ))
if estado == 1:
    valor = valor + (valor * 0.07)
    print(valor)
elif estado == 2:
    valor = valor + (valor * 0.12)
    print(valor)
elif estado == 3:
    valor = valor + (valor * 0.15)
    print(valor)
elif estado == 4:
    valor = valor + (valor * 0.08)
    print(valor)
else:
    print('Error. Invalid typed value')


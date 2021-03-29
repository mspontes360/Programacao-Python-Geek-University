"""
Faça um programa que leia um número inteiro positivo de três dígito ( de 100 a 999).
Gere outro número formado pelos dígito invertidos do número lido. Exemplo:
NumeroLido = 123
NumeroGerado = 321
"""

number_read = input("Enter a number between 100 and 999: ")
generated_number = number_read[::-1]

print(generated_number)
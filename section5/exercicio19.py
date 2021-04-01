'''
Faça um programa para verificar se um determinado número inteiro é divisível por
3 ou por, mas não simultaneamente pelos dois.
'''

print("Digite um número para verificar se ele é divisivel por 5 ou por 3")

numero = int(input("Digite um número :"))

if numero % 3 == 0:
    print(f'O número {numero} é divisível por 3')
elif numero % 5 == 0:
    print(f'O número {numero} é divisível por 5')
else:
    print(f'O número {numero} não é divisível por 3 ou por 5.')

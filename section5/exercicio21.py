'''
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).

Opção:
'''
print("Calculator")
print("Choose the option: \n1- Sum 2 numbers. \n2- Difference between 2 numbers (highest to lowest).")
print("3- Product between 2 numbers. \n4- Division between 2 numbers (the denominator cannot be zero).")

option = int(input("Option: "))

if option == 1:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    soma = number1 + number2
    print(f'The sum result is {soma}')
elif option == 2:
    number1 = int(input("Enter the largest number: "))
    number2 = int(input("Enter the smallest number: "))
    if number1 >= number2:
        difference = number1 - number2
        print(f'The result of the difference between the numbers is {difference}')
    else:
        print("Invalid operation, please restart the operation")
elif option == 3:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    product = number1 * number2
    print(f'The result of multiplication is {product}')
elif option == 4:
    number1 = int(input("Enter the largest number: "))
    number2 = int(input("Enter the smallest number: "))
    if number2 == 0:
        print("Invalid operation")
    else:
        division = number1 / number2
        print(f'The result of the division between the numbers is {division}')

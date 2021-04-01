"""
Faça um programaque receba a altura de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas (onde h corresponde à altura):
-- Homens: (72.7 * h) - 58
-- Mulheres: (62.1 * h) - 44.7

"""
name = input("Hello! What's your name? ").title()
print(f'Hello {name}!')

question = input("Let's find out your ideal weight? [Y / N] ").upper()

if question == 'Y':
    print('Okay!')
    gender = input('Enter your gender: [F / M] ').upper()
    if gender == 'F':
        height = float(input('Enter your height in centimeters: '))
        woman = (0.621 * height) - 44.7
        print(f'{name}, your ideal weight is: {woman} kg \nBye!')
    elif gender == 'M':
        height = float(input('Enter your height in centimeters: '))
        man = (0.727 * height) - 58
        print(f'{name}, your ideal weight is: {man} kg \nBye!')
    else:
        print('Invalid option, restart th program! \nBye!')
elif question == 'N':
    print('Bye')
else:
    print('Invalid option, restart the program!')


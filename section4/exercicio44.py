"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para
atingir seu objetivo.
"""

step_height = float(input("Enter the step height: "))
high = float(input("How high do you want to reach? "))

steps = high / step_height

print(f'The number of steps to climb is {steps}.')

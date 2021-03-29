"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

seconds = int(input("Enter a value in seconds: "))

hour = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
seconds_rest = rest % 60



print(f'{hour}:{minutes}:{seconds_rest}')


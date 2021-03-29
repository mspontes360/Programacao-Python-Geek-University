"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um
programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
quanto cada um ganharia com base no valor investido.
"""

friend_one = float(input("Enter the percentage invested by the first friend: "))
friend_two = float(input("Enter the percentage invested by the second friend: "))
friend_three = float(input("Enter the percentage invested by the third friend: "))

prize_amount = float(input("Enter the prize amount: "))

prize_friend_one = prize_amount * (friend_one / 100)
prize_friend_two = prize_amount * (friend_two / 100)
prize_friend_three = prize_amount * (friend_three / 100)

print(f'The friend one would win {prize_friend_one}.')
print(f'The friend two would win {prize_friend_two}.')
print(f'The friend three would win {prize_friend_three}.')





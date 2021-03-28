"""
A importância de R$ 780,000.00 será dividida entre três ganhadores de um
concurso. Sendo que a quantia total:
# O primeiro ganhador receberá 46%;
# O segundo receberá 32%;
# O terceiro receberá o restante.
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

first_winner = 780000.00 * 0.46
second_winner = 780000.00 * 0.32
third_winner = 780000.00 - first_winner - second_winner

print(f'The first winner will receive R$ {first_winner}.')
print(f'The second winner will receive R$ {second_winner}.')
print(f'The third winner will receive R$ {third_winner}.')



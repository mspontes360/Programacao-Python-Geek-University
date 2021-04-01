"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva a mensagem em função do preço novo (de
acordo com a segunda tabela).

PREÇO ANTIGO            PERCENTUAL DE AUMENTO
até R$50                        5%
entre R$50 e R$ 100             10%
acima de R$ 100                 15%


PREÇO NOVO                                  MENSAGEM
até R$80                                    Barato
entre R$ 80 e R$ 120 (inclusive)            Normal
entre R$ 120 e R$ 200 (inclusive)           Caro
acima de R$ 200                             Muito Caro
"""

old_price = float(input("Enter the old price: "))

if old_price <= 50.00:
    new_price = old_price + old_price * 0.05
elif old_price > 50.00 and old_price <= 100.00:
    new_price = old_price + old_price * 0.10
else:
    new_price = old_price + old_price * 0.15

if new_price <= 80.00:
    print(f'New price {new_price}, Cheap')
elif new_price > 80.00 and new_price <= 120.00:
    print(f'New price {new_price}, medium')
elif new_price > 120.00 and new_price <= 200.00:
    print(f'New price {new_price}, expensive')
else:
    print(f'New price {new_price}, very expensive')

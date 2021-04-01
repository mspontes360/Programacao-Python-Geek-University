"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do
distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo
de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o
custo ao consumidor.

CUSTO DE FÁBRICA                % DO DISTRIBUIDOR           % DOS IMPOSTOS
até R$ 12.000,00                        5                       isento
entre R$ 12.000,00 e 25.000,00          10                      15
acima de R$ 25.000,00                   15                      20
"""

factory_cost = float(input("Enter factory cost: "))

if factory_cost <= 0:
    print("Invalid cost!")
elif factory_cost < 12000.00:
    distributor = factory_cost * 0.05
    tax = 0
    cost_consumer = factory_cost + distributor + tax
    print(f'The cost to the consumer is {cost_consumer}.')
elif factory_cost >= 12000.00 and factory_cost <= 25000.00:
    distributor = factory_cost * 0.10
    tax = factory_cost * 0.15
    cost_consumer = factory_cost + distributor + tax
    print(f'The cost to the consumer is {cost_consumer}.')
else:
    distributor = factory_cost * 0.15
    tax = factory_cost * 0.20
    cost_consumer = factory_cost + distributor + tax
    print(f'The cost to the consumer is {cost_consumer}.')

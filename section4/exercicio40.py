"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá
ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

days_worked = float(input("Enter the number of days worked: "))

daily = 30.00
tax = 0.08
gross_amount = days_worked * daily
net_amount  = gross_amount - gross_amount * tax
print(f'The net amount he will receive is {net_amount}.')

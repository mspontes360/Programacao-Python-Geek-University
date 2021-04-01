"""
As tarifas de certo parque de estacionamento são as seguintes:
    # 1ª e 2ª R$ 1,00 cada
    # 3ª e 4ª R$ 1,40 cada
    # 5ª hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará "dez para a uma da tarde". Pretende-se criar
um programa que. lidos pelo teclado os momentos de chegada e da partida, escreva na
tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão
com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for 
superior à da partida, isso não é uma situação de erro. antes significará que a partida
ocorreu no dia seguinte ao da chegada.
"""

hour_arrival = int(input("Enter arrival time: "))
minute_arrival = int(input("Enter the minute of arrival: "))

hour_departure = int(input("Enter departure time: "))
minute_departure = int(input("Enter the minute of departure: "))

if hour_arrival > hour_departure:
    rest = 24 - hour_arrival
    total_hour = hour_departure + rest
else:
    total_hour = hour_departure - hour_arrival

if minute_arrival > minute_departure:
    #total_minute = minute_arrival + minute_departure - 60
    rest = 60 - minute_arrival
    total_minute = minute_departure + rest
    if total_minute > 0:
        total_hour = total_hour - 1
else:
    total_minute = minute_departure - minute_arrival

if total_minute > 0:
    total_hour = total_hour +1
    total_minute = 0

print(f'total time {total_hour} {total_minute}')

if total_hour <= 2:
    price = total_hour * 1.00
elif total_hour <= 4:
    price = total_hour * 1.40
else:
    price = total_hour * 2.00

print(f'price {price}')
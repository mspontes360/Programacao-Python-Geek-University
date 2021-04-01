"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:
    # Ter pelo menos 65 anos;
    # Ou ter trabalhado pelo menos 30 anos;
    # Ou ter menos de 60 anos e trabalhado pelo menos 25 anos.
"""

age = int(input("Enter the age: "))
service_time = int(input("Enter the service time: "))

if (age > 65) or (service_time >= 30) or (age < 60 and service_time >= 25):
    print("can retire")
else:
    print("Cannot retire")


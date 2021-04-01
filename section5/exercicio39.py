"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários
com menor salário terão um aumento proporcionalmente maior do que os funcionários
com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá
receber um bônus adicional de salário. Faça um programa que leia:

    # O valor do salário atual do fuuncionário;
    # O tempo de serviço desse funcionário na empresa ( número de anos de trabalho
      na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.

SALÁRIO ATUAL       REAJUSTE (%)        TEMPO DE SERVIÇO        BÔNUS
Até 500,00              25              abaixo de 1 ano       Sem bônus
Até 1000,00             20              de 1 a 3 anos           100,00
Até 1500,00             15              de 4 a 6 anos           200,00
Até 2000,00             10              de 7 a 10 anos          300,00
Acima de 2000,00    Sem reajuste        mais de 10 anos         500,00

"""

current_salary = float(input("Enter current salary: "))
length_service = float(input("Enter the length of service in the company: "))

if current_salary <= 0:
    print("Invalid information!")
elif current_salary <= 500.00:
    readjustment = current_salary + current_salary * 0.25
elif current_salary <= 1000.00:
    readjustment = current_salary + current_salary * 0.20
elif current_salary <= 1500.00:
    readjustment = current_salary + current_salary * 0.15
elif current_salary <= 2000.00:
    readjustment = current_salary + current_salary * 0.10
else:
    readjustment = current_salary

if length_service < 0:
    print("Invalid information!")
elif length_service < 1 :
    bonus = 0.00
elif length_service >= 1 and length_service <=3:
    bonus = 100.00
elif length_service >= 4 and length_service <=6:
    bonus = 200.00
elif length_service >= 7 and length_service <= 10:
    bonus = 300.00
else:
    bonus = 500.00

new_salary = readjustment + bonus

print(new_salary)
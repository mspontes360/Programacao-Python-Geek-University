"""
Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida.
Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro
(29 se o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia 31 nos
outros meses. Teste a validade do mês > 0 e mês < 13. Teste a validade do ano: ano <=
ano atual (use uma constante definida como o valor igual a 2021. Imprimir: "data válida"
ou "data inválida" no final da execução do programa.)

"""

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    year_leap = True

day = int(input("Insert the day: "))
month = int(input("Insert the month: "))
year = int(input("Insert the year: "))

CURRENT_YEAR = 2021

if day > 0 and 


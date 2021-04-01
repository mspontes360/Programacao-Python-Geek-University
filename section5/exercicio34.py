"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre a redução de conceito.

NOTA            CONCEITO (ATÉ 20 FALTAS)        CONCEITO (MAIS DE 20 FALTAS)
9.0 até 10.0                A                               B
7.5 até 8.9                 B                               C
5.0 até 7.4                 C                               D
4.0 até 4.9                 D                               E
0.0 até 3.9                 E                               E

"""

grade = float(input("Insert student's grade: "))
absence = float(input("Enter the number of student abscences: "))

if grade >= 9.0:
    if absence > 20:
        rank = "B"
    else: rank = "A"
elif grade >= 7.5 and grade <= 8.9:
    if absence > 20:
        rank = "C"
    else: rank = "B"
elif grade >= 5.0 and grade <= 7.4:
    if absence > 20:
        rank = "D"
    else: rank = "C"
elif grade >= 4.0 and grade <= 4.9:
    if absence > 20:
        rank = "E"
    else: rank = "E"
else:
    rank = "E"

print(f'The final rank of the student is: {rank}')
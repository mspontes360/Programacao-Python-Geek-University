"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o
intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionadas anteriormente obedece
aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame final: 5. De 
acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9),
de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações
necessárias.
"""

lab_work = float(input("Insert lab work assessment note: "))
semiannual_evaluation = float(input("Insert semiannual assessment note: "))
final_exam = float(input("Insert final exam assessment note: "))

final_grade = lab_work + semiannual_evaluation + final_exam

if final_grade >= 0 and final_grade <= 2.9:
    print("Student is failing")
elif final_grade >= 3.0 and final_grade <= 4.9:
    print("Student is recovering")
else:
    print("Student is approved")



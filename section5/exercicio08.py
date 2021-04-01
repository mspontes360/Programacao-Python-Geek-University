"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas
e exiba na tela a média destas notas. Um nota válida deve ser obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve
ser informado e o programa termina.
"""

first_note = float(input("Insert the first note: "))
second_note = float(input("Insert the second note: "))

if first_note >= 0 and first_note <= 10 and second_note >= 0 and second_note <= 10:
    average = (first_note + second_note) / 2
    print(average)
else:
    print("Invalid note!")

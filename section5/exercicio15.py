'''
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da
semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim
por diante.
'''

dia = int(input('Informe um número entre 1 a 7 referente ao dia da semana: '))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-Feira')
elif dia == 3:
    print('Terça-Feira')
elif dia == 4:
    print('Quarta-Feira')
elif dia == 5:
    print('Quinta-Feira')
elif dia == 6:
    print('Sexta-Feira')
elif dia == 7:
    print('Sábado')
else:
    print('Número inválido')

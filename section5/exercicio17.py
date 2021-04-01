'''
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
            A = (basemaior + basemenor) * altura / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.    
'''
print("Calculadora da área de trapézio")
baseMaior = int(input("Digite o valor da base maior: "))
baseMenor = int(input("Digite o valor da base menor: "))
altura = int(input("Digite o valor da altura: "))

if baseMaior == 0 or baseMenor == 0:
    print("Valor inválido")
else:
    A = ((baseMaior + baseMenor) * altura) / 2
    print(f'A área do trapézio é: {A}')

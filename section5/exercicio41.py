"""
Faça um algoritimo que calcule o IMC de uma pessoa e mostre sua classificação de
acordo com a tabela abaixo:

            IMC             Classificação
            <18.5           Abaixo do Peso
            18.6 - 24.9     Saudável
            25.0 - 29.9     Peso em excesso
            30.0 - 34.9     Obesidade Grau I
            35.0 - 39.9     Obesidade Grau II (severa)
            >= 40.0         Obesidade Grau III (mórbida)
"""

altura = float(input('Informe sua altura: '))

massa = float(input('Informe seu peso: '))

imc = massa / (altura ** 2)

print(f'Seu IMC é {imc}')

if imc < 18.5:
    print('Sua classificação é Abaixo do Peso')
elif imc > 18.6 and imc < 24.9:
    print('Sua classificação é Saudável')
elif imc > 25.0 and imc < 29.9:
    print('Sua classificação é Peso em excesso')
elif imc > 30.0 and imc < 34.9:
    print('Sua classificação é Obesidade Grau I')
elif imc > 35.0 and imc < 39.9:
    print('Sua classificação é Obesidade Grau II')
else:
    print('Sua classificação é Obesidade Grau III (mórbida)')

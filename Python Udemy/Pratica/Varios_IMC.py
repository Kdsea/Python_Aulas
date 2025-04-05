# Vamos calcular o IMC de várias pessoas, e depois vamos calcular a média do IMC
# IMC = peso / (altura * altura)
# IMC < 18.5 = Abaixo do peso
# IMC >= 18.5 e IMC < 25 = Peso normal
# IMC >= 25 e IMC < 30 = Sobrepeso
# IMC >= 30 e IMC < 35 = Obesidade grau 1
# IMC >= 35 e IMC < 40 = Obesidade grau 2
# IMC >= 40 = Obesidade grau 3

''' perguntar: quantas pessoas?
    repetir para cada pessoa:
    pedir peso
    pedir altura
    calcular IMC
    mostrar IMC e classificação
'''

# Definindo as variáveis
quantidade_pessoas = int(input('Quantas Pessoas?'))

#repetindo para cada pessoa:
for i in range(quantidade_pessoas):
    print(f"Pessoa {i + 1}")
    # pedindo pese e altura

    peso = float(input('Digite o Peso:'))
    altura = float(input('Digite a altura em metros:'))

    # Calculando IMC
    imc = peso / (altura ** 2)

    # Mostrando IMC e classificação
    print(f'IMC: {imc:.2f}')
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc >= 18.5 and imc < 25:
        print('Peso Normal')
    elif imc >= 25 and imc < 30:
        print('Sobrepeso')
    elif imc >= 30 and imc < 35:
        print('Obesidade grau 1')
    elif imc >= 35 and imc < 40:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')
    print('---')

    
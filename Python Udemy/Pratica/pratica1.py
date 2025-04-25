#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.

entrada = input('Digite um numero inteiro: ')

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é impar")
except ValueError:
    print("Isso nao é um numero inteiro")


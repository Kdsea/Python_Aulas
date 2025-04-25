# Operadores in e not in
# Strings são iteraveis, ou seja, podemos percorrer cada letra de uma string
# 0 1 2 3 4 5 
# K a u a d e
# -6-5-4-3-2-1
#nome = 'Kaude'
#print(nome[1])
#print(nome[-4])
#print('u' in nome)  True
#print('z' in nome)  False
#print('ola' not in nome)  True
#print('zero' in nome)  False

nome = input('Qual é o seu nome? ')
encontrar = input('Digite oque voce quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')
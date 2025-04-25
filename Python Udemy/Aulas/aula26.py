'''
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamento [::-1] - Inverte a string
Obs.: a funcao len() retorna o tamanho da string

'''

variavel = 'Olá Mundo'
print(variavel[4:]) # Mundo
print(variavel[:5]) # Olá M
print(len(variavel[-8:-2])) # Olá Mu
print(variavel[0:len(variavel):1]) # Olá Mundo
print(variavel[0:9:3]) # OaM
print(variavel[::-1]) # odnuM alO
"""
introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que vc digitar: ')

#try e except verifica se há erros no codigo, assim evitando do programa "estorar"
#ele lê até onde consegue e quando há erro ele pula para o proximo bloco que é o except
try:
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um numero')

#If e Else nao verificam erros
#if numero_str.isdigit: # "isdigit" checa se o usuario digitou apenas numeros
 #   numero_float = float(numero_str)
 #   print(f'O dobro de {numero_str} é {numero_float * 2}')
#else: 
 #   print('Isso não é um numero')
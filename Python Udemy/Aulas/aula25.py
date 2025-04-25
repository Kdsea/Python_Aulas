"""
s - string
d e i - int
f - float
.<numero de digito>f
x e X = Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Forçar o sinal a esquerda
Sinal - + ou, if
Conversion flags - !r !s !a
"""
variavel = 'ABC' 
print(f'{variavel}')
print(f'{variavel: >10}') # Preencheu com espaços a esquerda
print(f'{variavel: <10}') # Preencheu com espaços a direita
print(f'{variavel: ^10}') # Preencheu com espaços a direita e a esquerda
print(f'{10000.12323123:0>10,.2f}') # 10000.12
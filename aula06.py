# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo de dado em outro tipo de dado
# Python faz isso automaticamente, mas podemos fazer manualmente também
# Tipos imutáveis e primitivos
# str, int, float, bool
print(1 + 1) # soma de inteiros
#print('1' + 1) # erro, não é possível somar string com inteiro
print(int('1'), type(int('1'))) # converte string para inteiro e mostra o tipo
print(int('1') + 1) # converte string para inteiro e soma com 1
print(type(float('1') + 1)) # ele é executado de dentro para fora.
print(bool('1')) # string não vazia é True
print(bool(' ')) # string vazia é False
print(str(11) + 'b') # converte inteiro para string e concatena com 'b'

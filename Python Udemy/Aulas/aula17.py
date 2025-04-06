# if / elif       / else
# se / se não se / se não

#as condições serao testadas na ordem em que foram escritas
#se a primeira for verdadeira, as demais nao serao testadas
#se a primeira for falsa, a segunda sera testada e assim por diante
#se nenhuma for verdadeira, o else sera executado

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Este é o codigo do if')
elif condicao2:
    print('codigo para condicao 2')
elif condicao3:
    print('codigo para condicao 3')
elif condicao4:
    print('codigo para condicao 4')
else: 
    print('Nenhuma condicao foi atendida')

if 10 == 10:
    print('Outro If')

print('Fora do if')
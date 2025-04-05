
`altura:.2f # .2f diz quantas casa decimais deve aparecer

`nome = 'Kaua De Souza'
`altura = 1.95
`peso = 90
`imc = ...
`meu_imc = peso / (altura ** 2)

  

 F-strings são strings formatadas que permitem incluir expressões dentro de chaves {}

`linha_1 = f'{nome} tem {altura:.2f} de altura' com o f eu posso colocar variaveis dentro da string

`linha_2 = f'Pesa {peso} quilos' 'e seu IMC é'

`linha_3 = f'{meu_imc:.2f}' com o f eu posso colocar variaveis dentro da string

`print(linha_1)
`print(linha_2)
`print(linha_3)

Resultado no Console:

`Kaua De Souza tem 1.95 de altura
`Pesa 90 quilose seu IMC é
`23.67

[[Formatação de strings com o método format]]
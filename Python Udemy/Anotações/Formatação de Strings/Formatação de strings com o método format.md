Utilizar os Índices para aumentar a quantidade de Strings. Basicamente não dar uma ordem as strings apenas enumera-las exemplo abaixo.

`string = 'a={0} b={1} c={2:.2f}'

Parâmetro nomeado é quando dou um nome pras coisas dentro das criações das funções. Tudo que vier depois de um parâmetro nomeado deve ser nomeado

`string = 'a={0} b={1} c={nome3:.2f}'
`=a, b, nome3=c,`

`nome3` é um parâmetro

`a, b, c,` são argumentos

Quando a função está dentro de um objeto ela é chama de Método

`formato = string.format(
   `nome1=a, nome2=b, nome3=c
    `)

Codigo completo:

`a = 'A'
`b = 'B'
`c = 1.1

`string = 'a={nome1} b={nome2} c={nome3:.2f}'
`formato = string.format(
    `nome1=a, nome2=b, nome3=c
    `)
`print(formato)

[[Uma introdução às f-strings (formatação de strings)]]
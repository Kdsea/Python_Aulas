 If /        Elif        / Else
 Se / Se Não Se / Se não

Se você digitar oque é pedido você terá acesso Se Não você não terá acesso. Agora se não digitar nada ocorrerá um erro. 
Para entender melhor olhe o código abaixo

`nome = input('Qual o seu nome? ')
`entrada = input('Você quer entrar ou sair? ')

`if entrada == 'entrar':
    `print('Voce entrou no sistema')
    `print('Bem vindo', nome)
`elif entrada == 'sair':
    `print('Voce saiu do sistema')
`else:
    `print('Voce nao digitou nem "entrar" nem "sair"')
    `print('Acesso Negado!')

Um If pode ser executado sozinho, mas um Else não. Ele depende do If junto do Elif. Mas diferente do Else o Elfi pode se repetir quantas vezes quiser


Você terá 3 tipos de caminhos dependendo da sua resposta.

O primeiro se digitar entrar:

`Digite seu nome: kaua`
`Você quer entrar ou sair? entrar
`Voce entrou no sistema
`Bem vindo kaua

O segundo se digitar sair:

`Qual o seu nome? kaua
`Você quer entrar ou sair? sair
`Voce saiu do sistema

E o ultimo se não digitar nada:

`Você quer entrar ou sair? 
`Voce nao digitou nem "entrar" nem "sair"    
`Acesso Negado!

[[if, elif e else entendendo o fluxo do interpretador em condicionais]]




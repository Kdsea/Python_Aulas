# if / elif       / else
# se / se não se / se não
nome = input('Qual o seu nome? ')
entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Voce entrou no sistema')
    print('Bem vindo', nome)
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Voce nao digitou nem "entrar" nem "sair"')
    print('Acesso Negado!')
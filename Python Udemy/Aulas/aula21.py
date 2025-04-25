#Operadores lógicos and (e), or (ou), not (não)
#and - todas as condições precisam ser verdadeiras
#se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
#São considerados falsy 
#0 0.0 ' ' false
#tambem existe o tipo None que é usado para representar um não valor

#entrada = input('Você quer [E]ntrar ou [S]air? ').strip().upper()
#senha_digitada = input('Digite a senha: ')

#senha_permitida = '123456'

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    #print('Entrar')
#else:
    #print('Sair')

#Avaliação de curto-circuito
senha = input('Digite a senha: ') or 'Sem senha'
print(senha)
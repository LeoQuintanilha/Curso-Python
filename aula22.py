
# OPERADOR LÓGICO OR

#entrada = input('{E}ntrar  {S}air:')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'

#if entrada == 'E' and senha_digitada == senha_permitida:
#    print("Entrar!")

#else:
#    print("Sair")    

#O uso do OR significa que se algum valor 'verdadeiro' aparecer a sentença irá aparecer 'verdadeiro'.
# No caso abaixo, se eu digitar a senha será printada a senha ou se eu não digitar nada irá aparecer a mensagem 'Sem senha'.

senha = input('Senha: ') or 'Sem senha'
print(senha)



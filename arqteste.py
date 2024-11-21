entrada = input('{E}ntrar ou {S}air: ')

senha_digitada = input('Senha: ')

SENHA_DIGITADA = '123456'

if entrada == 'E' and senha_digitada == SENHA_DIGITADA:

    print('Você pode acessar o sistema.')
        
    idade = input('Qual a sua idade: ')
    nome = input('Qual o seu nome: ')
    idade_int = int(idade)

    ANO = 2024
    ano_nascimento = ANO - idade_int

    print('Seu nome é ', nome, ' sua idade é ', idade, 'e você nasceu no ano de ', ano_nascimento)
    print('Sua idade é: ', idade)

else:

    print('Você não pode acessar o sistema.')


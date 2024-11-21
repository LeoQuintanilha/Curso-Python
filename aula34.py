# REPETIÇÕES
# while (enquanto)
# Executa uma ação enquanto uma condição for verdadeira
# Loop infinito -> Quando um código não tem fim.

"""
senha = input('Qual a senha?')
condicao = '123456'
while condicao == senha:
    print(1)
    print(2)
    print(3)

else:
    print('Você não digitou a senha correta.')

"""

condicao = True

while condicao:
    nome = input('Qual o seu nome?')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
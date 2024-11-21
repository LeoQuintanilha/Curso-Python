# Operadores in e not in
# Strings são iteráveis, que nada mais é que eu posso mexer em cada caracter.
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
# Para eu saber qual o carater está incluído na posição 2 da variável nome temos que colocar o número entre [].

print('i' in nome)
# Utiliando o operador IN vamos saber se é Falso ou Verdadeiro se uma letra ou palavra esta contida na variável nome.

print('z' in nome)
# Utiliando o operador IN vamos saber se é Falso ou Verdadeiro se uma letra ou palavra esta contida na variável nome.

# O operador NOT IN é o inverso do IN.

nome_principal = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_principal:
    print(f'{encontrar} está em {nome_principal}')
else:
    print(f'{encontrar} não está em {nome_principal}')



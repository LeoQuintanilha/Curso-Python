'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário
não digite um número inteiro, informe que não é um número inteiro.
'''

print('Este é um programa para informar se um número digitado é par ou impar.')

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_Impar = entrada_int % 2 == 0
    print(f'O número {entrada_int} è `{}')

else:
    print('Você não digitou um número inteiro.')
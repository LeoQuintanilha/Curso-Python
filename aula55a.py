'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário
não digite um número inteiro, informe que não é um número inteiro.
'''

print('Este é um programa para informar se um número digitado é par ou impar.')

entrada = input('Digite um número: ')

if entrada == entrada * 2:
    print('Este é um número par.')

else:
    print('Este é um número Impar.')
"""
nome = input('Digite o seu nome: ')
nome_mae = input('Digite o nome da sua mãe: ')
nome_pai = input('Digite o nome do seu pai: ')
data_nascimento = input('Digite a sua data de nascimento: ')
endereco = input('Digite o seu endereço: ')

print('O cliente', nome, 'com a filiação', nome_mae, 'e', nome_pai, 'nascido em', data_nascimento, 'e com morada', endereco, 'está quite com suas obrigações eleitorais.')
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
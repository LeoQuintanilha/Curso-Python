nome = 'Edilene'
altura = 1.55
peso = 60
imc = peso / altura ** 2

frase1 = f'{nome} tem {altura:.2f} de altura e seu IMC é {imc:.2f}'

print(frase1)

print (nome, 'tem', altura, 'e seu IMC é', imc)
print (nome)

nome = input('Qual o seu nome?')
print(nome)
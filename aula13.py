nome = input('Qual o seu nome:')
altura = float(input('Qual a sua altura:'))
peso = int(input('Qual o seu peso:'))
imc = peso / altura ** 2

quadrado = altura ** 2

print(quadrado)

quadro = altura * altura

print(quadro)

if imc == 32:
    print('Tu estais no peso ideal.')

else:
    print('tu estais fora do seu peso.')

frase1 = f'{nome} tem {altura:.2f} de altura e seu IMC é {imc:.2f}'

print(frase1)

print (nome, 'tem', altura, 'e seu IMC é', imc)
print (nome)
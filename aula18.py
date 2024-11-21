# if / elif....... / else
# se / se não se   / se não 


condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:

    print('Esta afirmação é verdadeira')

elif condicao2:
    print('Código para condição 2')

elif condicao3 == True:
    print('Código para condição 3')

#Essa bola vermelha significa que o Python vai para a análise das condições nesta linha. No caso nem irá analisar esta linha. Só irá analisar a condição1 e condição2.

elif condicao3:
    print('Código para condição 3')

else:
    print("Nenhuma condição foi satisfeita!")

if 10 == 10:
    print('Outro if')
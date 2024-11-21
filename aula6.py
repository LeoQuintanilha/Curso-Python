# conversão de tipos, tambem chamado de oerção, type convertion, typecasting e coercion.
# É o ato de converter um tipo em outro. Por exemplo, as vezes queremos somar 2 valores
# Tipos imutáveis e primitivos: str, int, float, bool

print(1 + 1)
# Como Python é uma linguagem dinâmica, ela "percebe" que 1 é um int e o outro também e por isso faz a soma.

print('a' + 'b')
# Neste caso, o Python fará a união(Concatenou) destas 2 letras, sendo o resultado ab. Justo por ter identificado que não é um número inteiro e sim 2 strings.

# print('1' + 1)
# Tudo o que está dentro de aspas é uma string. Então o Python, como é de tipagem dinamica e forte.
# PHP e JavaScript são linguagem de tipagem dinâmica e fraca. No caso acima o PHP ou JS irá converter um dos valores. Já no Python, como é de tipagem dinâmica e forte irá lançar um erro.

print(int('1') + 1)
# Neste caso eu converti o primeiro valor para int pois está entre aspas e só então o Python identificou e conseguiu ler os 2 valores como int.

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

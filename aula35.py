while True:
    try:

        nota1 = float(input("Insira a nota 1: "))
        nota2 = float(input("Insira a nota 2: "))

        media = (nota1 + nota2) / 2

        if media >= 6:
            print("O aluno está aprovado.", media)

        else:
            print("O aluno não está aprovado.", media)

        break
    except ValueError:
        print('Digite valores númericos.')



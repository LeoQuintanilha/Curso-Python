while True:
    try:
        
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        
        media = (nota1 + nota2) / 2

        
        if media >= 6:
            print("Aprovado! Sua média é:", media)
        else:
            print("Reprovado! Sua média é:", media)

        
        break
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")
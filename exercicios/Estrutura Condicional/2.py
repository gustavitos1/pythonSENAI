while True:
    try:
        nota1 = int(input("insira a primeira nota: "))
        nota2 = int(input("insira a segunda nota: "))

        if nota1 < 0 or nota2 < 0 and nota1 > 100 or nota2 > 100:
            raise ValueError
    except ValueError:
        print("insira um valor entre 0 e 100")
    except TypeError:
        print("insira um numero")



        media = (nota1 + nota2) / 2

        if media > 0 and media < 70:
            print("reprovado")
        elif media >= 70 and media < 100:
            print("aprovado")

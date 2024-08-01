while True:
    try:
        escolha = int(input("escolha um numero de 1 a 12: "))

        resposta = ""

        if escolha == 1:
            resposta = "janeiro"
        elif escolha == 2:
            resposta = "feveiro"
        elif escolha == 3:
            resposta = "março"
        elif escolha == 4:
            resposta = "abril"
        elif escolha == 5:
            resposta = "maio"
        elif escolha == 6:
            resposta = "junho"
        elif escolha == 7:
            resposta = "julho"
        elif escolha == 8:
            resposta = "agosto"
        elif escolha == 9:
            resposta = "setembro"
        elif escolha == 10:
            resposta = "outubro"
        elif escolha == 11:
            resposta = "novembro"
        elif escolha == 12:
            resposta = "dezembro"
        else:
            break
    except ValueError:
        print("escolha invalida")
    except TypeError:
        print("escolha invalida")

print(f"o numero representa {resposta}")
while True:
    try:

        escolha = int(input("insira um numero de 1 a 7 que representara um dia da semana: "))



        if escolha == 1:
            print("domingo")
        elif escolha == 2:
            print("segunda")
        elif escolha == 3:
            print("terça")
        elif escolha == 4:
            print("quarta")
        elif escolha == 5:
            print("quinta")
        elif escolha == 6:
            print("sexta")
        elif escolha == 7:
            print("sabado")
        else:
            break
    except ValueError:
        print("invalido")

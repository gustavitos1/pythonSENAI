#aqui fazemos o while true para repetição do codigo caso o usuario erre
while True:
    #caso o usuario erre, o try except vai tornar a repetição possivel apartir do erro
    try:
        escolha = float(input("Digite um numero: "))

        if escolha > 0:
            print("positivo")
        elif escolha < 0:
            print("negativo")
        elif escolha == 0:
            print("neutro")
        else:
            break
    except ValueError:
        print("escreva um numero!")


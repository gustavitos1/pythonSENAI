while True:
    try:

        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        if numero1 > numero2:
            print("o primeiro numero é maior que o segundo")
        elif numero2 > numero1:
            print("o segundo é maior que o primeiro")
        else:
            break
    except ValueError:
        print("invalido")

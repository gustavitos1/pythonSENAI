while True:
    try:


        numero1 = int(input("Digite o primeiro numero inteiro: "))
        numero2 = int(input("Digite o segundo numero inteiro: "))
        numero3 = int(input("Digite o terceiro numero inteiro: "))



        if numero1 > numero2 and numero1 > numero3:
            print("o primeiro numero é o maior")
        elif numero2 > numero1 and numero2 > numero3:
            print("o segundo numero é o maior")
        elif numero3 > numero1 and numero3 > numero2:
            print("o terceiro numero é o maior")
        elif numero1 == numero2 == numero3:
            print("são iguais")
        else:
            break
    except ValueError:
        print("invalido, digite um numero!")
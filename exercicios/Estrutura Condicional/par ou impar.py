
import random

def jogo():


    print("Bem vindo ao jogo de par ou impar!")
    print("")
    print("-" * 20)
    print("faça sua aposta!")
    print("-" * 20)

    while True:
        escolha = input("par ou impar?: ")



        while True:
            try:
                numero = int(input("qual numero?: "))

                computador_numero = random.randint(0, 10)

                soma1 = numero + computador_numero

                soma = (numero + computador_numero) % 2




                if numero < 0 or numero > 10:
                    raise TypeError
                break
            except ValueError:
                print("invalido, digite outra vez")
            except TypeError:
                print("invalido, digite outra vez")

        if soma == 0:
            resultado = "par"
        else:
            resultado = "impar"





        print(f"você escolheu {numero} e o computador escolheu {computador_numero}")
        print(f"a soma é {soma1} e o resultado é {resultado}")
        if escolha == resultado:
            print("você venceu!")
        else:
            print("você perdeu!")

        jogar_denovo = input("deseja jogar novamente?s/n: ")

        if jogar_denovo == "n":
            break

jogo()




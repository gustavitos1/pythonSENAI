
#primeiro importe o random
import random
#agora crie o menu do jogo
replay = 0

while replay == 0:
    print("Bem vindo ao jogo da advinhação!")
    print('')
    print("-" * 20)
    print("")
    print('-' * 20)
    print("")
    print("irei falar um numero de 1 a 100")
    print('')
    print("tente adivinhar")

    #faça a geração do numero pela maquina
    numero_aleatorio = random.randint(1, 100)

    resposta = ""

    while True:
        try:
            print(resposta)
            escolha = int(input('qual você acha que é?: '))
            if escolha < numero_aleatorio:
                resposta = "é maior que isso"
            elif escolha > numero_aleatorio:
                resposta = "é menor que isso"
            else:
                print("meus parabens, você acertou o numero!")
                break
        except ValueError:
            print("erro, digite um numero!")


    replay = input("deseja jogar novamante?sim/não: ")
    while True:
        try:
            if replay == "sim" or replay == "não":
                break
        except ValueError:
            print("Tente novamente!")
    if replay == "sim":
        replay = 0
    else:
        replay = 1
print = "obrigado por jogar!"

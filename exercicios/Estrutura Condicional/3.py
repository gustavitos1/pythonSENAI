
while True:
    try:
        ano = int(input("coloque seu ano de nascimento: "))


        resposta = ""

        if ano < 2024 and ano >= 1920:
            break
        else:
            raise ValueError
    except ValueError:
        print("isso não é possivel, tente novamente")

idade = 2024 - ano

if idade < 18:
    resposta = "menor de idade"
elif idade >= 18:
    resposta = "maior de idade"
else:
    resposta = "invalido"


print(f"então você é {resposta}")
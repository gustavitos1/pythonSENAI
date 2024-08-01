
while True:
    try:
        renda = float(input("Qual o valor de sua renda anual: "))


        if renda <= 6.072:
            resposta = 0
        elif renda >= 56072.01 and renda <= 238.532:
            resposta = 7.05
        elif renda >= 238532.01 and renda <= 522.400:
            resposta = 15
        elif renda >= 522400.01 and renda <= 987.599:
            resposta = 22.50
        elif renda > 987.600:
            resposta = 27.50
        else:
            break
    except ValueError:
        print("invalido")

porcentagem = (renda * resposta) / 100

print(f"então {resposta}% é sua aliquota")

print(f"sera descontado de você R${porcentagem:.2f}")
print("Calculadora de Ohm")
print("escolha uma das opções:")
print("|tensão|1|<--")
print("|corrente|2|<--")
print("|resistencia|3|<--")
print("|resistencia do resistor|4|<--")
print("|sair|0|<--")

escolha = int(input("Escolha: "))



while escolha >= 0:

    if escolha == 1:
        print("tensão")
        print('')
        resistencia = float(input('digite o valor da resistencia em ohms: '))
        corrente = float(input('digite o valor da corrente em amperes: '))

        tensão = resistencia * corrente

        print(f"a tensão é de {tensão} volts")
    elif escolha == 2:
        print("corrente")
        print('')
        tensão = float(input('digite o valor da tensão em volts: '))
        resistencia = float(input('digite o valor da resistencia em ohms: '))

        corrente = tensão / resistencia

        print(f"a corrente é de {corrente} amperes")
    elif escolha == 3:
        print("resistencia")
        print('')
        tensão = float(input('digite o valor da tensão em volts: '))
        corrente = float(input('digite o valor da corrente em amperes: '))

        resistencia = tensão / corrente

        print(f"a resistencia é de {resistencia} Ω")
    elif escolha == 4:
        print("resistencia do resistor")
        print('')
        tensão_fonte = float(input("digite a tensão da fonte em volts: "))
        tensão_dispositivo = float(input("digite a tensão da dispositivo em volts: "))
        corrente = float(input("digite o valor da corrente em amperes: "))

        resistencia_resistor = (tensão_fonte - tensão_dispositivo) / corrente

        print(f"a resistencia do resistor é de {resistencia_resistor} Ω")
    else:
        print("escolha invalida")

        escolha = int(input("digite o numero da escolha: "))

        print("escolha novamente:")
        print("|tensão|1|<--")
        print("|corrente|2|<--")
        print("|resistencia|3|<--")
        print("|resistencia do resistor|4|<--")
        print("|sair|0|<--")







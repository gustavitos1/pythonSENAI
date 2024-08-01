def resistecia():
    while True:
        try:
            resistencia = float(input("insira o valor da resistencia em ohms: "))
            return resistencia
        except ValueError:
            print("insira um valor correto!")


def corrente():
    while True:
        try:
            corrente = float(input("insira o valor da corrente em amperes: "))
            return corrente
        except ValueError:
            print("insira um valor correto!")



def tensao():
    while True:
        try:
            tensao = float(input("insira o valor da tensão em volts: "))
            return tensao
        except ValueError:
            print("insira um valor correto!")


def tensao_fonte():
    while True:
        try:
            tensao_fonte = float(input("insira a tensão da fonte em volts: "))
            return tensao_fonte
        except ValueError:
            print("insira um valor correto!")


def tensao_dispositivo():
    while True:
        try:
            tensao_dispositivo = float(input("insira o valor da tensão do dispositivo em volts: "))
            return tensao_dispositivo
        except ValueError:
            print("insira um valor correto!")



def calculo_tensao(resistencia, corrente):
    tensao = resistencia * corrente
    return tensao


def calculo_resistencia(tensao, corrente):
    resistencia = tensao / corrente
    return resistencia


def calculo_corrente(tensao, resistencia):
    corrente = tensao / resistencia
    return corrente


def calculo_RR(tensao_dispositivo, tensao_fonte, corrente):
    resitencia_resistor = (tensao_fonte / tensao_dispositivo) / corrente
    return resitencia_resistor

def menu():
    while True:
        try:
            print("calculadora de ohms")
            print("escolha uma das opções abaixo: ")
            print("1 - tensão")
            print("2 - resistencia")
            print("3 - corrente")
            print("4 - resistencia do resistor")
            print("5 - sair")
            escolha = int(input("escolha: "))
            if escolha == 1:
                print(calculo_tensao(resistecia(), corrente()))
                break
            elif escolha == 2:
                print(calculo_resistencia(tensao(), corrente()))
                break
            elif escolha == 3:
                print(calculo_corrente(tensao(), resistecia()))
                break
            elif escolha == 4:
                print(calculo_RR(tensao_fonte(),tensao_dispositivo(), corrente()))
                break
            elif escolha == 5:
                print("tchau!")
                break
            else:
                raise ValueError
        except ValueError:
            print("insira um valor correto!")
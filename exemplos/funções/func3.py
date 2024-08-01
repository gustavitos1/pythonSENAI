def numero_1():
    while True:
        try:
            numero = int(input("Digite o primeiro numero: "))
            return numero
        except ValueError:
            print("insira um numero!")


def numero_2():
    while True:
        try:
            numero2 = int(input("Digite o segundo numero: "))
            return numero2
        except ValueError:
            print("insira um numero!")


def calculo_total(primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero
    subtracao = primeiro_numero - segundo_numero
    multiplicacao = primeiro_numero * segundo_numero
    divisao = primeiro_numero / segundo_numero

    print(f" a soma é {soma}\n a subtração é {subtracao}\n a multiplicação é {multiplicacao}\n a divisão é {divisao}")

def soma(primeiro_numero, segundo_numero):
    soma = primeiro_numero + segundo_numero
    return soma

def subtracao(primeiro_numero, segundo_numero):
    subtracao = primeiro_numero - segundo_numero
    return subtracao

def multiplicacao(primeiro_numero, segundo_numero):
    multiplicacao = primeiro_numero * segundo_numero
    return multiplicacao

def divisao(primeiro_numero, segundo_numero):
    divisao = primeiro_numero / segundo_numero
    return divisao



def menu(soma, subtracao, multiplicacao, divisao, calculo_total):
    while True:
        try:
            print('escolha uma das operações abaixo:')
            print('1 - Soma')
            print('2 - subtração')
            print('3 - multiplicação')
            print('4 - divisão')
            print('5 - todas')
            escolha = int(input("escolha um dos numeros em virtude da operação: "))

            if escolha == 1:
                print(soma(primeiro_numero, segundo_numero))
                break
            elif escolha == 2:
                print(subtracao(primeiro_numero, segundo_numero))
                break
            elif escolha == 3:
                print(multiplicacao(primeiro_numero, segundo_numero))
                break
            elif escolha == 4:
                print(divisao(primeiro_numero, segundo_numero))
            elif escolha == 5:
                calculo_total(primeiro_numero, segundo_numero)
                break
            else:
                raise ValueError
        except ValueError:
            print("insira somente os valores mencionados! ")


primeiro_numero = numero_1()
segundo_numero = numero_2()
menu(soma, subtracao, multiplicacao, divisao, calculo_total)

def peso():
    while True:
        try:
            peso = float(input("Digite um peso: "))
            return peso
        except ValueError:
            print("digite um valor inteiro!")

def altura():
    while True:
        try:
            altura = float(input("Digite uma altura: "))
            return altura
        except ValueError:
            print("digite um valor inteiro!")

peso = peso()
altura = altura()

def imc(peso, altura):
    imc = peso * (altura * altura)
    if imc > 0 and imc < 18.5:
        print("seu indice de massa corporal é de magreza")
    elif imc >= 18.5 and imc < 24.9:
        print("seu indice de massa corporal é normal")
    elif imc >= 25 and imc < 29.9:
        print("seu indice de massa corporal é de sobrepeso")
    elif imc >= 30 and imc < 34.9:
        print("aqui ja começa a obesidade de grau I")
    elif imc >= 35 and imc < 39.9:
        print("aqui ja é obesidade de grau II")
    elif imc > 40:
        print("aqui representa obesidade de grau III")
    else:
        print("invalido")

imc(peso, altura)
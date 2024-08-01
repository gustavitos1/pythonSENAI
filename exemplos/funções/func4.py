def lado_direito():
    while True:
        try:
            direito = float(input('escreva o lado da parte direita do triangulo: '))
            return direito
        except ValueError:
            print("escreva um numero!")

def lado_esquerdo():
    while True:
        try:
            esquerdo = float(input('escreva o lado da parte esquerda do triangulo: '))
            return esquerdo
        except ValueError:
            print("escreva um numero!")

def base():
    while True:
        try:
            base = float(input('escreva o lado da base do triangulo: '))
            return base
        except ValueError:
            print("escreva um numero!")


direito = lado_direito()
esquerdo = lado_esquerdo()
base = base()


def calculo_lados(direito, esquerdo, base):
    if direito == esquerdo == base:
        print("o triangulo é equilatero")
    elif direito == esquerdo and direito != base:
        print("o triangulo é isoceles")
    elif esquerdo == base and direito != base:
        print("o triangulo é isoceles")
    else:
        print('o triangulo é escaleno')

calculo_lados(direito, esquerdo, base)

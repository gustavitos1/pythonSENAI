
def colocar_temperatura():
    while True:
        try:
            celsius = float(input('Informe a temperatura em graus Celsius: '))
            return celsius
        except ValueError:
            print('Informe um valor em graus Celsius: ')

celsius = colocar_temperatura()
def kelvin():
    conversão = celsius + 273
    return conversão

def fahrenheit():
    conversão = celsius * 1.8 + 32
    return conversão

def exibir_conversão(kelvin, fahrenheit):
    while True:
        try:
            escolha = int(input('Informe o valor 1 para kelvin e 2 para fahrenheit: '))

            if escolha == 1:
                print(kelvin(),"essa é a temperatura em graus kelvin.")
                break
            elif escolha == 2:
                print(fahrenheit(),"essa é a temperatura em graus fahrenheit")
                break
            else:
                raise ValueError
        except ValueError:
            print("insira somente os numeros mencionados!")



exibir_conversão(kelvin, fahrenheit)
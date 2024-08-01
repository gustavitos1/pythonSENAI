from datetime import datetime

def pedir_nome():
    nome = input('Digite seu nome: ')
    return nome
def hora_atual():
    hora = datetime.now().hour
    if hora >= 0 and hora <= 5:
        return 'boa madrugada'
    elif hora >= 5 and hora <= 12:
        return 'bom dia'
    elif hora >= 12 and hora <= 19:
        return 'boa tarde'
    else:
        return 'boa noite'

print(hora_atual(), pedir_nome())
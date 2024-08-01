import datetime
dia = datetime.datetime.now().day
mes = datetime.datetime.now().month
ano = datetime.datetime.now().year
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
segundo = datetime.datetime.now().second
semana = datetime.datetime.now().isoweekday()
resposta = ""
answer = ""
dia_semana = ""


if mes == 1:
    resposta = "janeiro"
elif mes == 2:
    resposta = "fevereiro"
elif mes == 3:
    resposta = "março"
elif mes == 4:
    resposta = "abril"
elif mes == 5:
    resposta = "maio"
elif mes == 6:
    resposta = "junho"
elif mes == 7:
    resposta = "julho"
elif mes == 8:
    resposta = "agosto"
elif mes == 9:
    resposta = "setembro"
elif mes == 10:
    resposta = "outubro"
elif mes == 11:
    resposta = "novembro"
elif mes == 12:
    resposta = "dezembro"
else:
    print("Erro")

if hora < 12 and hora >= 6:
    answer = "bom dia"
elif hora >= 12 and hora < 18:
    answer = "boa tarde"
elif hora >= 18 and hora < 12:
    answer = "boa noite"
elif hora >= 0 and hora < 6:
    answer = "bom madrugada"
else:
    print("Erro")

if semana == 1:
    dia_semana = "segunda-feira"
elif semana == 2:
    dia_semana = "terça-feira"
elif semana == 3:
    dia_semana = "quarta-feira"
elif semana == 4:
    dia_semana = "quinta-feira"
elif semana == 5:
    dia_semana = "sexta-feira"
elif semana == 6:
    dia_semana = "sabado"
elif semana == 7:
    dia_semana = "domingo"
else:
    print("Erro")

nome = input('Qual o seu nome?: ')
print(f"{answer} {nome}   \nhoje é {dia_semana} dia {dia} de {resposta} de {ano}   \n{hora}:{minuto}:{segundo}")
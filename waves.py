import requests
import datetime
from datetime import timedelta
import time
import pytz
import mail
import json

url = "https://surfguru.pictures/dados/praia.php?id=40"
teste = False
ultimo = ""
sleep = 1800
tz = pytz.timezone('America/Sao_Paulo')
dow = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']

while True:
    now = datetime.datetime.now(tz=tz)
    dia = now.strftime('%Y-%m-%d')
    hora = now.strftime('%H')
    print(now.strftime('%Y-%m-%d %H:%M:%S'), "Verificando")
    if (hora >= "17" and dia != ultimo):
        print(now.strftime('%Y-%m-%d %H:%M:%S'), "Enviando")
        ultimo = dia
        page = requests.get(url, headers={'User-Agent': 'XYZ/3.0'}).content
        j = json.loads(page)

        mask = "[{fData}] Alt {fOnda:.1f}m / Temp {fTemp}ºC / Per {fPer:.0f}s / Pot {fPot:.1f}\n"
        previsao = ""
        for i in range(0, 4):
            data = now + timedelta(days=i)
            hOnda = int(j['dados'][i]['surf']['h3']) / 10
            hTemp = j['dados'][i]['temper']['h3']
            hPer = int(j['dados'][i]['periodo']['h3']) / 10
            hPot = int(j['dados'][i]['pototal']['h3']) / 10
            previsao += mask.format(fData=dow[data.weekday()],
                                    fOnda=hOnda, fTemp=hTemp, fPer=hPer, fPot=hPot)

        print(previsao)
        mail.send(['alexsetta@gmail.com'], "Previsão Ondas", previsao)

    print(now.strftime('%Y-%m-%d %H:%M:%S'), "Aguardando próxima execução")
    if (teste):
        break
    time.sleep(sleep)
    continue

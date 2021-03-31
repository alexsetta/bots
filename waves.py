from bs4 import BeautifulSoup
import requests
import time
import mail 

class Wave(object):
	def __init__(self, size, direction):
		self.size = size
		self.direction = direction
    
	def normalize(self, txt):
		return txt.replace(" ", "").replace("\n", "")

	def show(self):
		txt = "Tamanho: {size} - Direção: {direction}"
		return txt.format(size=self.size, direction=self.direction)

w = Wave("", "")
url = "https://www.waves.com.br/surf/ondas/picos/maxim/"
teste = False
ultimo = ""
sleep = 1800

while True:
	dia =  time.strftime('%Y-%m-%d', time.localtime())
	hora = time.strftime('%H', time.localtime())
	print(dia, hora, "Verificando")
	if (hora < "06" and dia == ultimo):
		print("Aguardando próxima janela")
		time.sleep(sleep)
		continue

	print(dia, hora, "Enviando")
	ultimo = dia
	page = requests.get(url, headers={'User-Agent': 'XYZ/3.0'}).content
	soup = BeautifulSoup(page, "html.parser")

	results = soup(id="forecast_wave_size")	
	rows = results[0].findAll("span")
	w.size = w.normalize(rows[0].get_text())
	
	results = soup(id="forecast_wave_direction")	
	w.direction = w.normalize(results[0].get_text())
	
	mail.send(['alexsetta@gmail.com'], "Previsão para hoje", w.show())
	time.sleep(sleep)



	

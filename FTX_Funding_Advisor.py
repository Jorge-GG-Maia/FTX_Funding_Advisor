import time, requests, json
import pandas as pd
import numpy as np
import telebot

# Carregamento e leitura do arquivo de configurações
Config = pd.read_csv('Config.csv')

MonitorList = np.array(Config['LIST_OF_FUTURES'])
if MonitorList[0] == 'all':
	MonitorList = []

periodo = float(Config['UPDATE_DELAY'][0])
quantidade = int(Config['OUTPUT_NUMBER'][0])
thres = float(Config['OUTPUT_THRESHOLD'][0])

token = str(Config['TELEGRAM_TOKEN'][0])
chat = str(Config['TELEGRAM_CHAT_ID'][0])

print(token)
print(chat)

#Ínicio do laço de repetição dos ciclos 

while True:
	
	valores = pd.DataFrame()
	retorno = requests.get(url = 'https://ftx.com/api/funding_rates')
	r = retorno.json()
	if len(MonitorList) == 0:
		for i in range(0, len(r['result'])):
			MonitorList.append(r['result'][i]['future'])


	if r['success'] == True:
	
		future = []
		rate = []
		tempo = []
		for i in range(0, len(r['result'])):
			if r['result'][i]['future'] in MonitorList:
				future.append(r['result'][i]['future'])
				rate.append(r['result'][i]['rate'])
				tempo.append(r['result'][i]['time'])
			else:
				continue

		future = np.array(future)
		rate = np.array(rate)
		tempo = np.array(tempo)

		valores['future'] = future
		valores['rate'] = rate
		valores['time'] = tempo


		valores = valores.drop_duplicates(subset = ['future'])
		valores = valores[abs(valores['rate']) >= thres]

		valores = valores.sort_values(['rate'], ascending = False)
		nomes = np.array(valores['future'])
		funding = np.array(valores['rate'])

		print('\n', time.asctime())

		topx = []
		print('\n''TOP X: ')
		for i in range(0, quantidade):
			print(nomes[i] ,'(', funding[i] ,')')
			topx.append(str(nomes[i] + '(' + str(funding[i]) + ')'))

		valores = valores.sort_values(['rate'], ascending = True)
		nomes = np.array(valores['future'])
		funding = np.array(valores['rate'])

		bottonx = []
		print('\n''BOTTON X: ')
		for i in range(0, quantidade):
			print(nomes[i] ,'(', funding[i] ,')')
			bottonx.append(str(nomes[i] + '(' + str(funding[i]) + ')'))	


			
		bot = telebot.TeleBot(token)

		bot.send_message(chat, time.asctime())
		
		bot.send_message(chat, 'Top X:')
		for i in range(0, quantidade):
				bot.send_message(chat, topx[i])
		bot.send_message(chat, 'Botton X:')
		for i in range(0, quantidade):
			bot.send_message(chat, bottonx[i])


		time.sleep(periodo)

	else:
		print('\n''Erro 404 - Não foi possível estabelecer conexão com endpoint')
		break



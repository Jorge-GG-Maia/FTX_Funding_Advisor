import pandas as pd
import numpy as np

DFConfig = pd.DataFrame()

futures = str(input('Insira a lista de instrumentos a monitorar, separados por vírgula''\n'))
if futures == '':
	futures = 'all'

delay = str(input('Insira o delay, em segundos, desejado''\n'))
if delay == '':
	delay = 3600

output = str(input('Insira a quantidade de instrumentos a serem exibidos''\n'))
if output == '':
	output = 3

threshold = str(input('Insira o Output Threshold''\n'))
if threshold == '':
	threshold = 0

token = str(input('Insira o telegram token''\n'))
chat = str(input('Insira o telegram chat id''\n'))

LFutures = futures.split(', ')

LFutures = np.array(LFutures)
delay = np.array(delay)
output = np.array(output)
threshold = np.array(threshold)

token = np.array(token)
chat = np.array(chat)

DFConfig['LIST_OF_FUTURES'] = LFutures
DFConfig['UPDATE_DELAY'] = delay
DFConfig['OUTPUT_NUMBER'] = output
DFConfig['OUTPUT_THRESHOLD'] = threshold

DFConfig['TELEGRAM_TOKEN'] = token
DFConfig['TELEGRAM_CHAT_ID'] = chat

print(DFConfig)


DFConfig.to_csv('Config.csv', index = False)



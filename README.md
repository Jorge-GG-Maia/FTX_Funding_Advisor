# FTX_Funding_Advisor
Bot para monitoramento dos Funding Rates integrado ao Telegram

As seguintes bibliotecas são nescessárias para utilização adequada do script, caso não possua alguma delas instalada estão todas disponíveis pelo comando "pip install". :

time requests pandas json numpy telebot

Para iniciar o uso da aplicação, deve-se primeiro executar o arquivo Config.py, no qual serão inseridas as configurações desejadas, sendo elas:

LIST_OF_FUTURES: Lista de nomes dos instrumentos para monitorar. Use: "all" para todas. Padrão: all

UPDATE_DELAY: Delay, em segundos, entre cada checagem/report. Padrão: 3600

OUTPUT_NUMBER: A quantidade de instrumentos a se mostrar (maiores e menores). Exemplo: se OUTPUT_NUMBER=3 então deve-se mostrar a lista dos 3 maiores e 3 dos menores funding rates. Padrão: 3

OUTPUT_THRESHOLD: Se o valor absoluto do funding rate for menor que OUTPUT_THRESHOLD, então o instrumento deve ser omitido da saída (apenas mostre na saída instrumentos com funding rate > OUTPUT_THRESHOLD). Padrão: 0

TELEGRAM_TOKEN = Token telegram. 

TELEGRAM_CHAT_ID = Chat_id telegram. 

Espaços deixados em branco serão preenchidos com o valor padrão automaticamente

Após preencher as configurações, um arquivo chamado "Config.csv" será gerado armazenando as variáveis

Uma vez concluído este passo, pode-se então executar o arquivo FTX_Funding_Advisor.py, ele importará as configurações e começará o monitoramento em tempo real de acordo com as configurações estabelecidas anteriormente.

Formato de saída:

**[Data - Hora]

  Top X:

  Nome_do_instrumento (funding_rate)

  Nome_do_instrumento (funding_rate)

  Nome_do_instrumento (funding_rate)

  ...

  Nome_do_instrumento (funding_rate)

  Bottom X:

  Nome_do_instrumento (funding_rate)

  Nome_do_instrumento (funding_rate)

  Nome_do_instrumento (funding_rate)

  ...

  Nome_do_instrumento (funding_rate)**

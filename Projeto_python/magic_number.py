'''Intuito do projeto:
Desenvolver uma calculadora que mostra quantos fundos imobiliários será necessário para conseguir um novo fundo sem ter que comprar com recursos próprios'''

# perquisar as bibliotecas em python necessárias para execução do projeto


import yfinance as yf
import pandas_datareader.data as pdr
import pandas as pd

yf.pdr_override()

'''ticker_symbol = 'HGLG11.SA'

data_inicial = '2024-01-01'
data_final = '2024-05-10'

tabela_cotacao = pdr.get_data_yahoo('HGLG11.SA', data_inicial, data_final)

print(tabela_cotacao)'''


tabela_fii_data = '2024-01-01'
tabela_fii_info = pdr.get_data_yahoo('HGLG11.SA', tabela_fii_data)
#tabela_fii_history = pdr.get_data_yahoo.history(period='1d')

print(tabela_fii_info)
#print(tabela_fii_history)

'''import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")'''

# fazer a lógica da calculadora
# desenvolver o código
# manter as cotas atualizadas 
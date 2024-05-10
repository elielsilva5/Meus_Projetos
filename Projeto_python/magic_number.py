'''Intuido do projeto:
Desenvolver uma calculadora que mostra quantos fundos imobiliários será necessário para conseguir um novo fundo sem ter que comprar com recursos próprios'''

# perquisar as bibliotecas em python necessárias para execução do projeto


'''import yfinance as yf

ticker_symbol = 'HGLG11.SA'

fii_data = yf.Ticker(ticker_symbol)
fii_info = fii_data.info
fii_hystory = fii_data.history(period = '1d')

print(fii_info)
print(fii_hystory)'''

import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")

# fazer a lógica da calculadora
# desenvolver o código
# manter as cotas atualizadas 
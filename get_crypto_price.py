import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

if not os.path.exists('./datasets/crypto_price.csv'):
    df = pd.DataFrame(columns=['Timestamp', 'BTC', 'ETH'])
    df.to_csv('datasets/crypto_price.csv', index=False)


url = 'https://tw.stock.yahoo.com/cryptocurrencies'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

btc = soup.find_all('span', class_='Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)')[0].text
btc = float(btc.replace(',', ''))

eth = soup.find_all('span', class_='Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)')[2].text
eth = float(eth.replace(',', ''))

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

df_prices = pd.read_csv('datasets/crypto_price.csv')
df_prices = df_prices.astype({'BTC': float, 'ETH': float})
index = len(df_prices)
df_prices.loc[index, 'Timestamp'] = current_time
df_prices.loc[index, 'BTC'] = btc
df_prices.loc[index, 'ETH'] = eth

df_prices.to_csv('datasets/crypto_price.csv', index=False)
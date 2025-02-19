import csv
import requests
import symbols

from dotenv import load_dotenv
load_dotenv()

import os
token = os.environ.get("ALPHA_VENTAGE_API_KEY")

def getAllStocksData():
    stockSymbols = symbols.getStockSymbols()
    stocks = []
    counter = 1

    for symbol in stockSymbols:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={token}'
        r = requests.get(url)
        data = r.json()
        print(f"Stock: {counter}")
        print(data)
        counter = counter + 1
        stocks.append(data)

getAllStocksData()
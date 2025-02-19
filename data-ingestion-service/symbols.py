import csv
import requests

from dotenv import load_dotenv
load_dotenv()

import os
token = os.environ.get("ALPHA_VENTAGE_API_KEY")

def getStockSymbols():
    CSV_URL = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={token}'
    symbols = []

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            symbols.append(row[0])

    return symbols
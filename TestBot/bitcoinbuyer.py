# Print bitcoin price

import requests

url = "https://data.alpaca.markets/v1beta3/crypto/us/bars?symbols=BTC%2FUSD&timeframe=1Day&limit=1000&sort=asc"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

# Look at previous week's 

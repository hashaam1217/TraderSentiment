# Print bitcoin price
import time
import requests

url = "https://data.alpaca.markets/v1beta3/crypto/us/bars?symbols=BTC%2FUSD&timeframe=1Day&limit=1000&sort=asc"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

#  buy bitcoin

url = "https://paper-api.alpaca.markets/v2/orders"

payload = {
    "symbol": "BTC/USD",
    "qty":  "0.0001",
    "side": "buy",
    "type": "market",
    "time_in_force": "gtc"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "APCA-API-KEY-ID": "PKG18B6O6AJJ3T3Z4GPJ",
    "APCA-API-SECRET-KEY": "bvQw5otydDb7ax9cdSJHYDpME4nr1MS7s6uOImzJ"
}
count = 0

while (count < 1000):
    time.sleep(1)
    count += 1
    response = requests.post(url, json=payload, headers=headers)
    print(count)
    print(response.text)

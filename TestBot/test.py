import requests

url = "https://paper-api.alpaca.markets/v2/account"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": "PKG18B6O6AJJ3T3Z4GPJ",
    "APCA-API-SECRET-KEY": "bvQw5otydDb7ax9cdSJHYDpME4nr1MS7s6uOImzJ"
}

response = requests.get(url, headers=headers)

print(response.text)

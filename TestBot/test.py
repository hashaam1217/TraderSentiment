import requests

url = "https://broker-api.sandbox.alpaca.markets/v2/orders"

api_key = "CKCE9FV33AXIH7SZ1CBE"
api_secret = "b2vQmHOQOaXWPsNSkW771y84q9N8EqMY8OHPyasa"


headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": api_key,
    "APCA-API-SECRET-KEY": api_secret
}

response = requests.get(url, headers=headers)

print(response.text)

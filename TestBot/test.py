import requests

url = "https://broker-api.sandbox.alpaca.markets/v2/account"


#    KEY: "CKORSRQHYMMEHPEODEHU"
#    SECRET_KEY: "XJgVmGGiaMNb8PlBfMgCHfbiADOtXEHujLl9jYZL"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": "CKORSRQHYMMEHPEODEHU",
    "APCA-API-SECRET-KEY": "XJgVmGGiaMNb8PlBfMgCHfbiADOtXEHujLl9jYZL"
}

response = requests.get(url, headers=headers)

print(response.text)

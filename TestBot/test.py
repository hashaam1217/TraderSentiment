import alpaca_trade_api as tradeapi

# authentication and connection details
api_key = 'CKORSRQHYMMEHPEODEHU'
api_secret = 'XJgVmGGiaMNb8PlBfMgCHfbiADOtXEHujLl9jYZL'
APCA_API_BASE_URL = 'https://broker-api.sandbox.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, APCA_API_BASE_URL)

# obtain account information
account = api.get_account()
print(account)

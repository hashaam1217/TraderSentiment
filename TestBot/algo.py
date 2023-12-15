import alpaca_trade_api as tradeapi

# authentication and connection details
api_key = "CKCE9FV33AXIH7SZ1CBE"
api_secret = "b2vQmHOQOaXWPsNSkW771y84q9N8EqMY8OHPyasa"
base_url = "https://broker-api.sandbox.alpaca.markets"

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

aapl = api.get_asset('AAPL', 'day')

# obtain account information
# account = api.get_account()
# print(account)

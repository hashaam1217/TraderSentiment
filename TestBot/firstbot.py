# Create a small bot that buys or sells based on info

import alpaca_trade_api as tradeapi

api_key = "PKG18B6O6AJJ3T3Z4GPJ"
secret_key = "bvQw5otydDb7ax9cdSJHYDpME4nr1MS7s6uOImzJ"

api = tradeapi.REST(api_key, secret_key)

quote = api.get_latest_quote('AAPL')

print(quote)

print(f"AAPL bid price: {round(quote.bp)}")


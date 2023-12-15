import alpaca_trade_api as tradeapi

paperurl = "https://paper-api.alpaca.markets"

APCA_API_BASE_URL="https://paper-api.alpaca.markets"

APCA_API_KEY_ID="CKORSRQHYMMEHPEODEHU"

APCA_API_SECRET_KEY="XJgVmGGiaMNb8PlBfMgCHfbiADOtXEHujLl9jYZL"

api = tradeapi.REST(APCA_API_KEY_ID,APCA_API_SECRET_KEY,paperurl,api_version='v1')

account = api.get_account()

print(account) #shows $0 account, created 2019, everything else looks good

api.submit_order('TSLA', 1, 'buy', 'market', 'day')

import requests
import json

coinbase_response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json")

data = json.loads(coinbase_response.content.decode("utf-8"))

bitcoin_price = data['bpi']['USD']['rate_float']
print(bitcoin_price)

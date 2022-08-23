import requests
import json


def get_bitcoin_price():

    coinbase_response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json")

    data = json.loads(coinbase_response.content.decode("utf-8"))

    bitcoin_price = data['bpi']['USD']['rate_float']

    return bitcoin_price
    # print(bitcoin_price)

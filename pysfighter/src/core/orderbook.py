import requests
import json
import StringIO
import pysfighter

def orderbook(venue, stock):
    response = requests.get("https://api.stockfighter.io/ob/api/venues/"+venue+"/stocks/"+stock).text
    response = json.load(StringIO.StringIO(response))
    orders = pysfighter.Object()
    orders.venue = venue
    orders.symbol = stock
    orders.bids = list()
    orders.asks = list()
    for bid in response["bids"]:
        new_bid = pysfighter.Object()
        new_bid.price = bid["price"]
        new_bid.qty = bid["qty"]
        orders.bids.append(new_bid)
    for ask in response["bids"]:
        new_ask = pysfighter.Object()
        new_ask.price = ask["price"]
        new_ask.qty = ask["qty"]
        orders.asks.append(new_ask)
    orders.timestamp = str(response["ts"])
    return orders
import requests
import json
import StringIO
import pysfighter

def quote(venue, stock):
    response = requests.get("https://api.stockfighter.io/ob/api/venues/"+venue+"/stocks/"+stock+"/quote").text
    response = json.load(StringIO.StringIO(response))
    orders = pysfighter.Object()
    orders.venue = venue
    orders.symbol = stock
    orders.bid = response["bid"]
    orders.ask = response["ask"]
    orders.bidSize = response["bidSize"]
    orders.askSize = response["askSize"]
    orders.bidDepth = response["bidDepth"]
    orders.askDepth = response["askDepth"]
    orders.last = response["last"]
    orders.lastSize = response["lastSize"]
    orders.lastTrade = str(response["lastTrade"])
    orders.quoteTime = str(response["quoteTime"])
    return orders